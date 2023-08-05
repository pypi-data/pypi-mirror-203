import functools
import operator
import os
from typing import IO


def prod(iterable, initial=1):
    return functools.reduce(operator.mul, iterable, initial)


def align(alignment: int, position: int) -> int:
    assert alignment & (alignment - 1) == 0
    mask = alignment - 1
    return (position + mask) & ~mask


def align_down(alignment: int, position: int) -> int:
    assert alignment & (alignment - 1) == 0
    mask = alignment - 1
    return position & ~mask


def samefile_copy(f, src: int, dst: int, length: int, block_size: int = 1 << 18):
    if src < dst:
        src += length
        dst += length
        while length:
            to_read = min(length, block_size)
            src -= to_read
            dst -= to_read
            length -= to_read
            f.seek(src)
            data = f.read(to_read).ljust(to_read, b"\0")
            f.seek(dst)
            f.write(data)

    else:  # src > dst
        while length:
            to_read = min(length, block_size)
            length -= to_read
            f.seek(src)
            data = f.read(to_read).ljust(to_read, b"\0")
            f.seek(dst)
            f.write(data)
            src += to_read
            dst += to_read


def get_file_size(file: IO) -> int:
    return os.fstat(file.fileno()).st_size
