from pathlib import Path
from typing import Dict, IO, Tuple
import zipfile

import attr
from fickle import Unknown, UnknownImport
from fickle.ext.pytorch import fake_torch_load_zipped, StoredTensor, StorageManagerZip
from pure_safetensors import DType, SafeTensors, SafeTensorInfo
from pure_safetensors.numpy import NumpyAdapter
import tqdm

import json


class NontrivialTensorLayoutError(RuntimeError):
    """
    This error happens if the tensor layout is nontrivial.
    """


class InplaceConversionError(RuntimeError):
    """
    This error happens if there are issues preventing in-place tensor file conversion.
    """


@attr.s(eq=False)
class _TensorConversionInfo:
    stored_tensor: StoredTensor = attr.ib()
    dtype: DType = attr.ib()
    shape: Tuple[int] = attr.ib()


@attr.s(eq=False)
class PyTorchSafetensorsConverterBase:
    safe_tensors: SafeTensors
    torch_checkpoint: IO

    def _sanitize_json(self, obj):
        if isinstance(obj, (str, int, float, bool)) or obj is None:
            return obj
        elif isinstance(obj, (tuple, list)):
            return tuple(self._sanitize_json(x) for x in obj)
        elif isinstance(obj, dict):
            return {
                str(self._sanitize_json(k)): self._sanitize_json(v)
                for k, v in obj.items()
            }
        elif isinstance(obj, UnknownImport):
            return str(obj)
        elif isinstance(obj, Unknown):
            return self._sanitize_json(attr.asdict(obj, recurse=False))

        return repr(obj)

    def convert_metadata(self, metadata: dict):
        return {
            key: json.dumps(self._sanitize_json(value))
            for key, value in metadata.items()
        }

    def convert_and_store_tensor(self, key: str, info: _TensorConversionInfo):
        m = self.safe_tensors.as_buffer()
        m[key][0][:] = info.stored_tensor.buffer

    def get_tensor_conversion_info(self, key: str, stored_tensor: StoredTensor):
        if not stored_tensor.has_trivial_layout:
            raise NontrivialTensorLayoutError(
                f"tensor {key} has size {stored_tensor.size} and nontrivial layout "
                f"{stored_tensor.stride} which is not supported"
            )
        dtype = NumpyAdapter.NUMPY_DTYPES_MAP[stored_tensor.storage.dtype]
        return key, _TensorConversionInfo(
            stored_tensor=stored_tensor, dtype=dtype, shape=stored_tensor.size
        )

    def get_pytorch_metadata_and_tensors(self):
        d = fake_torch_load_zipped(self.torch_zip_file)
        if type(d.get("state_dict", None)) is dict:
            state_dict = d.pop("state_dict", None)
        else:
            # in a newer version of the checkpoint format, they seem to dispense with
            # the metadata entirely and just have pure tensors in the pickle file
            state_dict = d
            d = {}
        return self.convert_metadata(d), state_dict

    def prepare(self):
        self.torch_zip_file = zipfile.ZipFile(self.torch_checkpoint)
        self.metadata, state_dict = self.get_pytorch_metadata_and_tensors()
        self.tensor_conversion_info: Dict[str, _TensorConversionInfo] = dict(
            self.get_tensor_conversion_info(key, stored_tensor)
            for key, stored_tensor in state_dict.items()
        )


@attr.s(eq=False)
class PyTorchSafetensorsInplaceConverter(PyTorchSafetensorsConverterBase):
    torch_checkpoint: IO = attr.ib()
    safe_tensors_kwargs: dict = attr.ib(factory=dict)

    def _tensor_conversion_info_to_safetensorinfo(
        self, tci: _TensorConversionInfo
    ) -> SafeTensorInfo:
        # figure out tensor offset in the zip file
        t = tci.stored_tensor
        storage_manager = t.storage_manager
        if not isinstance(storage_manager, StorageManagerZip):
            raise InplaceConversionError("storage should be zip file")

        with t.open_storage() as f:
            if f._decompressor is not None:
                raise InplaceConversionError(
                    f"tensor zip archive member {t.storage.key} is compressed"
                )
            if f._decrypter is not None:
                raise InplaceConversionError(
                    f"tensor zip archive member {t.storage.key} is encrypted"
                )
            zip_tensor_offset = f._orig_compress_start

        sti = SafeTensorInfo(
            dtype=tci.dtype,
            shape=tci.shape,
            start=zip_tensor_offset,
            end=zip_tensor_offset + t.size_in_bytes,
        )
        if sti.start % sti.dtype.recommended_alignment_in_bytes != 0:
            raise InplaceConversionError(f"tensor {sti!r} is improperly aligned")

        return sti

    def real_convert_inplace(self):
        self.prepare()

        tensors = (
            (key, self._tensor_conversion_info_to_safetensorinfo(tci))
            for key, tci in self.tensor_conversion_info.items()
        )
        tensors = list(
            tqdm.tqdm(tensors, unit="tensor", total=len(self.tensor_conversion_info))
        )

        self.safe_tensors = self._make_inplace_safetensors()
        file_map = self.safe_tensors.FileMap(self.safe_tensors.settings)
        file_map.tensors.update(tensors)
        file_map.validate()
        file_map.metadata = self.metadata

        # assigning to the filemap does not actually trigger a file write
        self.safe_tensors.map = file_map

        # move tensors if necessary to make room for the header
        self.safe_tensors.create_or_replace_or_delete_tensors({})

    def _make_inplace_safetensors(self):
        return SafeTensors(
            self.torch_checkpoint,
            do_not_initialize_map=True,
            mode="r+",
            **self.safe_tensors_kwargs,
        )

    @classmethod
    def convert_inplace(cls, torch_checkpoint: Path):
        with open(torch_checkpoint, "r+b") as f:
            instance = cls(torch_checkpoint=f)
            instance.real_convert_inplace()


@attr.s(eq=False)
class PyTorchSafetensorsConverter(PyTorchSafetensorsConverterBase):
    torch_checkpoint: IO = attr.ib()
    safe_tensors: SafeTensors = attr.ib()

    def real_convert_file_to_file(self):
        self.prepare()
        tensor_conversion_info = self.tensor_conversion_info

        self.safe_tensors.metadata = self.metadata

        # allocate space
        self.safe_tensors.as_buffer().update(
            (key, (None, info.dtype, info.shape))
            for key, info in tensor_conversion_info.items()
        )

        total_bytes = sum(
            inf.stored_tensor.size_in_bytes for inf in tensor_conversion_info.values()
        )
        with tqdm.tqdm(
            total=total_bytes, unit="B", unit_scale=True, unit_divisor=1024
        ) as pbar:
            for key, info in tensor_conversion_info.items():
                self.convert_and_store_tensor(key, info)
                self.safe_tensors.flush(free=True)
                pbar.update(info.stored_tensor.size_in_bytes)

    @classmethod
    def convert_file_to_file(cls, torch_checkpoint: Path, safe_tensors: Path):
        with open(torch_checkpoint, "rb") as f, SafeTensors(safe_tensors, "x+") as st:
            instance = cls(torch_checkpoint=f, safe_tensors=st)
            instance.real_convert_file_to_file()
