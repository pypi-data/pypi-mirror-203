import functools
import json
import os
import struct
from typing import Dict, IO, Iterable, List, Optional, Tuple

import attr
import marshmallow
from marshmallow import fields
import sortedcollections
import warnings

from .mmap import (
    FakeMemoryMappingFactory,
    MemoryMapping,
    MemoryMappingFactory,
    RealMemoryMappingFactory,
    mmap,
)
from .exc import SafeTensorError, SafeTensorHeaderError, SafeTensorEmptyFileError
from .util import align, prod, samefile_copy

try:
    import sparsefile
except ImportError:
    sparsefile = None


# you can use this global variable to control whether the OS mmap is used
use_mmap = mmap is not None


@attr.s(eq=False)
class SafeTensors:
    """
    This object is not thread-safe, and safetensor file structure should not be
    modified by different threads or processes at the same time.

    Resizing the file may result in a crash:
    https://stackoverflow.com/questions/19545949/detect-that-mmap-ed-file-has-been-truncated

    Parameters
    ----------
    file: str, file-like, or Path
        File to operate on.
    mode: {"r", "r+", "x+", "w+", "c"}
        r: Open existing file for reading only.
        r+: Open existing file for reading and writing.
        w+: Create or overwrite existing file for reading and writing.
        c: Copy-on-write: assignments affect data in memory, but changes are
           not saved to disk. The file on disk is read-only.
    sparse: bool or None, optional
        If True, make the file sparse. If False, then don't. If None, then
        try to make it sparse but don't raise an exception if it's not possible
        to do so.
    use_mmap: bool, optional
        Use mmap? Default value depends on whether it is supported.
    do_not_initialize_map: bool, optional
        If True, do not read or write the file header on instance init. This is
        used for PyTorch checkpoint in-place conversion, and I don't know
        what else you could be using it for (default: False).
    """

    _valid_modes = frozenset(("r", "r+", "x+", "w+", "c"))

    file: IO = attr.ib()
    mode: str = attr.ib()
    sparse: bool = attr.ib(default=None)
    settings: "Settings" = attr.ib(factory=lambda: Settings(), kw_only=True)
    use_mmap: bool = attr.ib(factory=lambda: use_mmap)
    do_not_initialize_map = attr.ib(default=False)

    mappings: Dict[str, MemoryMapping] = attr.ib(init=False, factory=dict)

    map: "FileMap"
    tensors: "Dict[str, SafeTensorInfo]"
    _memory_mapping_factory: MemoryMappingFactory

    _close_on_exit: bool = False

    def _open_file(self):
        self.file = open(self.file, self.mode.replace("c", "r") + "b")

    def __attrs_post_init__(self):
        if not hasattr(self.file, "read"):
            # the user passed in a Path or str, so we need to make sure to close it
            self._open_file()
            self._close_on_exit = True

        # replace "x+" with "w+" since they are equivalent after the file is created
        if self.mode == "x+":
            self.mode = "w+"

        self._init_memory_mapping_factory()

        # load file or write empty header if creating new file
        if not self.do_not_initialize_map:
            self._initialize_structure()

    def _init_memory_mapping_factory(self):
        cls = RealMemoryMappingFactory if self.use_mmap else FakeMemoryMappingFactory
        self._memory_mapping_factory = cls(file=self.file, mode=self.mode)

    @mode.validator
    def check(self, attribute, value):
        if value not in self._valid_modes:
            raise ValueError(f"{value!r} not in {self._valid_modes!r}")

    def assert_writable(self):
        mode = self.mode
        if mode == "c" or mode == "r":
            raise AssertionError(
                "operation not supported since file opened with mode={mode!r}"
            )

    def __enter__(self):
        return self

    def __exit__(self, exc_type, exc_value, traceback):
        self.close()

    def close(self):
        self.flush(free=True)
        if self._close_on_exit:
            self.file.close()

    def _initialize_structure(self):
        if self.mode != "w+":
            try:
                self._read_header()
            except SafeTensorEmptyFileError:
                # if the file is totally empty and mode == "r+" (read+write), then
                # just initialize the file
                if self.mode == "r+":
                    self._write_empty_header()
                else:
                    raise
        else:
            self._write_empty_header()

    def _write_empty_header(self):
        self._write_header(FileMap(settings=self.settings))

    def _write_header(self, file_map):
        self.assert_writable()
        # temporarily destroy the file header to prevent usage of a broken file
        # if the moves below fail
        self.file.seek(0)
        self.file.write(b"\0\0\0\0\0\0\0\0")

        for move in file_map.pending_moves:
            samefile_copy(self.file, src=move.src, dst=move.dst, length=move.len)

        self.file.seek(0)
        self.file.write(file_map.header)

        self.map = file_map

    def _read_header(self):
        m = self.FileMap.from_file(self.file, settings=self.settings)
        file_size = self.file.seek(0, os.SEEK_END)

        min_size = m.minimum_file_size
        if file_size < min_size:
            raise SafeTensorError(f"actual file too short, {file_size} < {min_size}")

        self.map = m

    @property
    def metadata(self):
        """
        Do not mutate this property! Make a copy and then assign to this property.
        """
        return self.map.metadata

    @metadata.setter
    def metadata(self, metadata):
        new_map = self.map.copy()
        new_map.metadata = metadata
        new_map.modify()  # move tensors if necessary
        self._write_header(new_map)

    @property
    def tensors(self):
        """
        Do not mutate this property! Make a copy and then assign to this property.
        """
        return self.map.tensors

    def as_numpy(self, **kw):
        """
        Examples
        --------

        ::
            with SafeTensors(...) as st, st.as_numpy() as st_numpy:
                do_stuff(st_numpy["my_tensor_name"] * 3 + 1)
                st_numpy.update({"new_tensor": my_array, "another_tensor": my_array_2})
                del st_numpy["my_tensor_name"]
        """
        from .numpy import NumpyAdapter

        return NumpyAdapter(self, **kw)

    def as_buffer(self, **kw):
        from .adapter import BufferAdapter

        return BufferAdapter(self, **kw)

    def create_or_replace_or_delete_tensors(
        self, tensors: "Dict[str, Optional[SafeTensorInfo]]"
    ) -> None:
        """
        Allocate tensors. This may resize the JSON header, and sometimes even
        move existing tensors to make way for a larger header. As such, it is NOT
        safe to use this method if you have existing memory mappings.

        If a tensor is ``None``, then it will be deleted.

        Existing tensors (with the same name) will be replaced/moved.
        """
        self.assert_writable()

        file_map = self.map.copy()
        file_map.modify(
            create={
                name: tensor for name, tensor in tensors.items() if tensor is not None
            },
            delete={name for name, tensor in tensors.items() if tensor is None},
        )

        self.file.seek(file_map.minimum_file_size)
        self.file.write(b"\0")
        self.file.flush()
        self._write_header(file_map)
        self.truncate()
        self.sparsify()

    def truncate(self):
        """
        Truncate file to its smallest possible size.
        """
        self.assert_writable()
        n = self.map.minimum_file_size
        self.file.seek(n)
        self.file.write(b"\0")
        self.file.flush()
        self.file.truncate(n)

    def sparsify(self):
        """
        Make file sparse, depending on the value of :attr:`sparse`.
        """
        self.assert_writable()
        if self.sparse is False:
            return

        if sparsefile is None:
            text = (
                "module `sparsefile` not available, cannot "
                "make file sparse to save space"
            )
            if self.sparse is None:
                warnings.warn(text)
                return
            else:
                raise AssertionError(text)

        for start, end in self.map.get_empty_ranges():
            length = end - start
            if self.sparse is None:
                # opportunistic
                if not sparsefile.maybe_sparse(self.file, start, length):
                    # failed to make it sparse, give up
                    break
            else:
                sparsefile.ensure_sparse(self.file, start, length)

    def _open_memory_mapping(self, offset: int, length: int) -> MemoryMapping:
        return self._memory_mapping_factory.map(offset=offset, length=length)

    def get_memory_mapping_for_tensor(
        self, key: str
    ) -> "Tuple[SafeTensorInfo, MemoryMapping]":
        """
        Map the tensor given by ``key`` in memory.
        """
        tensor = self.tensors[key]
        mapping = self.mappings.get(key, None)
        if mapping is None:
            self.mappings[key] = mapping = self._open_memory_mapping(
                offset=tensor.start, length=tensor.end - tensor.start
            )
        return (tensor, mapping)

    def flush(self, keys=None, free: bool = False) -> None:
        """
        Ensure that tensor data is written to disk. If ``free == True``, then
        remove the memory mapping from the cached memory mappings.
        """
        mappings = self.mappings
        keys = tuple(mappings.keys()) if keys is None else keys
        for key in keys:
            mapping = mappings.get(key, None)
            if mapping is not None:
                mapping.flush()
                if free:
                    mappings.pop(key, None)


@attr.s
class DType:
    name: str = attr.ib()
    kind: str = attr.ib()
    size_in_bytes: int = attr.ib()
    numpy_name: str = attr.ib()
    recommended_alignment_in_bytes: int = attr.ib(default=None)

    def __attrs_post_init__(self):
        if self.recommended_alignment_in_bytes is None:
            self.recommended_alignment_in_bytes = max(8, self.size_in_bytes)

    def __str__(self):
        return self.name


_dtypes_list = [
    DType("BOOL", "b", 1, "bool"),
    DType("BF16", "bf", 2, "bfloat16"),
]
_dtypes_list += (DType(f"U{n * 8}", "u", n, f"uint{n * 8}") for n in (1, 2, 4, 8))
_dtypes_list += (DType(f"I{n * 8}", "i", n, f"int{n * 8}") for n in (1, 2, 4, 8))
_dtypes_list += (DType(f"F{n * 8}", "f", n, f"float{n * 8}") for n in (2, 4, 8))
dtypes = {dt.name: dt for dt in _dtypes_list}
del _dtypes_list


class NonnegativeInteger(fields.Integer):
    def _deserialize(self, value, attr, data, **kwargs):
        if not isinstance(value, int) or value < 0:
            raise self.make_error("invalid", input=value)
        return super()._deserialize(value, attr, data, **kwargs)


class SafeTensorSchema(marshmallow.Schema):
    class Meta:
        unknown = marshmallow.RAISE

    dtype = fields.String(required=True)
    shape = fields.List(NonnegativeInteger(), required=True)
    data_offsets = fields.Tuple(
        (NonnegativeInteger(), NonnegativeInteger()), required=True
    )

    @marshmallow.post_load
    def dataclass_post_load(self, data, **kwargs):
        header_size = self.context["safetensors_header_size"]
        a, b = data["data_offsets"]

        # if it's a zero-length tensor, place it at the very beginning
        if a == b:
            a = b = 0

        if b < a:
            raise marshmallow.ValidationError(
                "tensor end position > tensor start position", "data_offsets"
            )

        return SafeTensorInfo(
            dtype=dtypes[data["dtype"]],
            shape=data["shape"],
            start=a + header_size,
            end=b + header_size,
        )

    @marshmallow.pre_dump
    def dataclass_pre_dump(self, data, **kwargs):
        if type(data) is dict:
            # leave it as-is
            return data

        header_size = self.context["safetensors_header_size"]

        # if it's a zero-length tensor, place it at the very beginning
        a = data.start - header_size
        b = data.end - header_size
        if a == b:
            a = b = 0

        # this is required for estimating header sizes
        if a < 0:
            # make it invalid on purpose
            a = 1
            b = 0

        return dict(
            dtype=str(data.dtype),
            shape=data.shape,
            data_offsets=(a, b),
        )


class SafeTensorsSchema(marshmallow.Schema):
    class Meta:
        unknown = marshmallow.RAISE

    tensors = fields.Dict(
        fields.String(), fields.Nested(SafeTensorSchema), required=True
    )
    metadata = fields.Dict(fields.String(), fields.String(), required=False)

    @marshmallow.pre_load
    def pre_load_metadata_split(self, data, **kwargs):
        if type(data) is not dict:
            raise marshmallow.ValidationError("root object must be dictionary")

        split = {"tensors": data.copy()}
        try:
            split["metadata"] = split["tensors"].pop("__metadata__")
        except KeyError:
            pass  # metadata is optional

        return split

    @marshmallow.post_dump
    def post_dump_metadata_split(self, data, **kwargs):
        if type(data) is not dict:
            raise marshmallow.ValidationError("root object must be dictionary")

        merged = data["tensors"].copy()
        if "__metadata__" in merged:  # check for conflict
            raise marshmallow.ValidationError("cannot have tensor named __metadata__")

        try:
            merged["__metadata__"] = data["metadata"]
        except KeyError:
            pass  # metadata is optional

        return merged


@attr.s(eq=False)
class Settings:
    header_size_alignment: int = attr.ib(default=4096)
    header_size_padding: int = attr.ib(default=1024)
    new_tensor_alignment: int = attr.ib(default=64)
    maximum_header_size: int = attr.ib(default=100_000_000)
    maximum_file_size: int = attr.ib(2 ** 40)


@attr.s
class MoveRequest:
    src: int = attr.ib()
    dst: int = attr.ib()
    len: int = attr.ib()


def sorted_tensors_dict(values=()):
    return sortedcollections.ValueSortedDict(lambda value: value.start, values)


@attr.s
class FileMap:
    settings: Settings = attr.ib()
    metadata: Optional[Dict[str, str]] = attr.ib(default=None)
    tensors: "Dict[str, SafeTensorInfo]" = attr.ib(factory=sorted_tensors_dict)
    pending_moves: List[MoveRequest] = attr.ib(factory=list)

    _header = None

    @attr.s
    class _Header:
        """
        Internal class used for header data construction.
        """

        header_size: int = attr.ib()
        json_data: bytes = attr.ib()

        @property
        def unpadded_length(self):
            """
            Length of the 8-byte length specified plus the JSON data, without padding.
            """
            return len(self.json_data) + 8

        @property
        def fits(self):
            return self.unpadded_length <= self.header_size

        def __bytes__(self):
            """
            The length of the returned bytes object will always be :attr:`header_size`.
            """
            assert self.fits, "data cannot fit inside header"
            json_size = self.header_size - 8
            return struct.pack("<q", json_size) + self.json_data.ljust(json_size)

    @staticmethod
    def _parse_size(data):
        if len(data) < 8:
            raise SafeTensorError("header too small")
        return struct.unpack("<q", data)[0]

    def _load_header(self, header: bytes):
        json_size = self._parse_size(header[:8])
        header_size = json_size + 8

        if header_size < 10:
            raise SafeTensorError("header size cannot be less than 10")

        if len(header) != header_size:
            raise SafeTensorError("header length inconsistent with size inside header")

        data = self._schema(header_size).load(json.loads(header[8:]))

        metadata = data.get("metadata", None)
        tensors = sorted_tensors_dict(data["tensors"])

        self.metadata = metadata
        self.tensors = tensors

    @property
    def header(self):
        """
        Reading this attribute generates a header or returns the cached current header.
        Writing to this attribute parses the header information into this object.
        """
        if self._header is None:
            self._header = self._get_header()
        return self._header

    @header.setter
    def header(self, value: Optional[bytes]):
        if value is None:
            self._header = None
            return

        self._header = value
        self._load_header(value)

    @header.deleter
    def header(self):
        self._header = None

    @classmethod
    def from_file(cls, f, settings: Settings, **kw):
        f.seek(0)
        length_data = f.read(8)
        if not length_data:
            raise SafeTensorEmptyFileError
        json_size = cls._parse_size(length_data)

        # check size constraint
        header_size = json_size + 8
        if header_size > settings.maximum_header_size:
            raise SafeTensorHeaderError(
                f"size too large, {header_size} > {settings.maximum_header_size}"
            )

        json_data = f.read(json_size)

        instance = cls(settings=settings, metadata=None, tensors=None, **kw)
        instance.header = length_data + json_data
        instance.validate()
        return instance

    def copy(self):
        kw = attr.asdict(self, recurse=False)
        kw["tensors"] = kw["tensors"].copy()
        return type(self)(**kw)

    @staticmethod
    def _schema(header_size):
        return SafeTensorsSchema(context={"safetensors_header_size": header_size})

    def _get_header_for_header_size(self, header_size: int) -> "_Header":
        data = {"tensors": self.tensors}

        if self.metadata is not None:
            data["metadata"] = self.metadata

        return self._Header(
            header_size=header_size,
            json_data=json.dumps(
                self._schema(header_size=header_size).dump(data)
            ).encode("utf-8"),
        )

    def _get_header(self) -> bytes:
        """
        Return the header as a bytestring.

        This is particularly annoying because the JSON content depends on the length of
        the header, which must be large enough to contain the JSON content. Thankfully,
        the length of the JSON is monotonically decreasing with the header size.
        """
        if self.tensors:
            first_tensor_offset = self.tensors.values()[0].start
        else:
            first_tensor_offset = 0

        # This produces the maximum number of bytes that will be required
        # to represent this JSON, but a _potentially_ smaller overall header.
        largest_json_header = self._get_header_for_header_size(0)

        # Premature optimization: avoid redundant call to _get_header_for_header_size
        if first_tensor_offset == 0:
            # In this case they are the same.
            smallest_json_header = largest_json_header
        else:
            # This is the smallest possible header in terms of bytes of JSON.
            smallest_json_header = self._get_header_for_header_size(first_tensor_offset)

        if smallest_json_header.fits:
            # Let's try to reduce the amount of padding.

            if largest_json_header.unpadded_length <= first_tensor_offset:
                # This larger-JSON header would still fit, so let's use it.
                final_header = self._get_header_for_header_size(
                    largest_json_header.unpadded_length
                )
            else:
                # The larger-JSON header would overlap with the first tensor,
                # so revert back to the smallest-JSON header.
                final_header = smallest_json_header
        else:
            # The smallest possible header size would still exceed the available
            # space. Since tensors must be moved, make enough room so that
            # this movement doesn't need to happen again too soon.
            header_size = self.compute_reserved_header_space(
                largest_json_header.unpadded_length
            )
            final_header = self._get_header_for_header_size(header_size)

        return bytes(final_header)

    def compute_reserved_header_space(self, header_size: int) -> int:
        return align(
            self.settings.header_size_alignment,
            header_size + self.settings.header_size_padding,
        )

    @property
    def header_size(self):
        return len(self.header)

    def validate(self):
        prev_end = self.header_size
        for name, tensor in self.tensors.items():
            start = tensor.start
            end = tensor.end

            req_size = tensor.required_size
            if req_size != end - start:
                raise SafeTensorError(
                    f"tensor {name!r} {tensor!r} size is wrong, expected {req_size}"
                )

            if start != end:
                # only check tensors of nonzero size

                if start < prev_end:
                    raise SafeTensorError(
                        f"tensor {name!r} overlaps with previous structure"
                    )

            prev_end = end

        if prev_end > self.settings.maximum_file_size:
            raise SafeTensorError(
                f"last tensor position {prev_end} exceeds maximum file size"
            )

    @property
    def minimum_file_size(self):
        tensors = self.tensors
        p = tensors.values()[-1].end if tensors else 0
        return max(p, self.header_size)

    def get_empty_ranges(self):
        ranges = []
        prev_end = self.compute_reserved_header_space(self.header_size)

        for name, tensor in self.tensors.items():
            start = tensor.start
            end = tensor.end

            if start == end:
                continue  # ignore empty tensors

            if prev_end >= end:
                continue

            if prev_end > start:
                start = prev_end

            # this is stupid
            if prev_end != start:
                ranges.append((prev_end, start))

            prev_end = end

        return ranges

    def _allocate_tensors(self, tensors: "Iterable[SafeTensorInfo]"):
        tensors_decreasing = list(tensors)
        tensors_decreasing.sort(key=lambda t: t.required_size, reverse=True)

        # sorted from smallest to largest
        empty_ranges = sortedcollections.SortedList(
            self.get_empty_ranges(), key=lambda r: r[1] - r[0]
        )

        for tensor in tensors_decreasing:
            req_size = tensor.required_size
            if req_size == 0:
                tensor.start = tensor.end = 0
                continue

            while True:
                if not empty_ranges:
                    empty_ranges.add((self.minimum_file_size, float("inf")))

                free_start, free_end = empty_ranges.pop()

                alignment = max(
                    tensor.dtype.recommended_alignment_in_bytes,
                    self.settings.new_tensor_alignment,
                )
                tensor_start = align(alignment, free_start)
                if tensor_start + req_size <= free_end:
                    # we have room, place it here
                    tensor.start = tensor_start
                    free_start = tensor.end = tensor_start + req_size
                    empty_ranges.add((free_start, free_end))
                    break

    def modify(
        self,
        create: "Dict[str, SafeTensorInfo]" = {},
        delete: "Iterable[str]" = (),
    ) -> None:
        """
        Allocate tensors. This may resize the JSON header, and sometimes even
        move existing tensors to make way for a larger header. As such, it is NOT
        safe to use this method if you have existing memory mappings.

        Notes
        -----
        This invokes a modified version of an awful greedy algorithm.

        https://en.wikipedia.org/wiki/First-fit-decreasing_bin_packing
        """

        for name in delete:
            self.tensors.pop(name, None)

        for name in create.keys():
            self.tensors.pop(name, None)

        new_tensor_set = frozenset(create.keys())

        # modified first-fit decreasing algorithm
        self._allocate_tensors(create.values())
        for name, tensor in create.items():
            self.tensors[name] = tensor

        try:
            # We need to keep looping because it's possible that the header is now too
            # large because tensors got moved towards the end of the file.
            while True:
                # Get new header size.
                del self.header
                header_size = self.header_size

                # Determine the tensors that need to be moved because they overlap
                # with the header.
                misplaced_tensors = {
                    (name, tensor.copy(), tensor.start, tensor.end)
                    for name, tensor in self.tensors.items()
                    if tensor.start < header_size and not tensor.is_zero_length
                }

                # End the loop if there are no tensors to move.
                if not misplaced_tensors:
                    break

                # Find new positions for these tensors.
                self._allocate_tensors([t[1] for t in misplaced_tensors])

                for name, new_tensor, _, _ in misplaced_tensors:
                    self.tensors[name] = new_tensor

                # Add to the list of pending moves.
                self.pending_moves.extend(
                    MoveRequest(src=old_start, dst=t.start, len=t.end - t.start)
                    for name, t, old_start, old_end in misplaced_tensors
                    if name not in new_tensor_set
                )
        except:
            # Prevent use of broken tensor locations
            self.tensors = None
            raise


SafeTensors.FileMap = FileMap


@attr.s(eq=False)
class SafeTensorInfo:
    dtype: DType = attr.ib()
    shape: Tuple[int, ...] = attr.ib(converter=tuple)
    start: int = attr.ib()
    end: int = attr.ib()

    def copy(self):
        return type(self)(**attr.asdict(self, recurse=False))

    @property
    def is_zero_length(self):
        return self.start == self.end

    @functools.cached_property
    def required_size(self):
        return prod(self.shape, self.dtype.size_in_bytes)
