from __future__ import annotations
from argparse import ArgumentParser, FileType, Namespace
from functools import partial
from hashlib import algorithms_available, new
from io import BufferedReader
from typing import IO, Generic, Protocol, Type, TypeVar


CHUNK_SIZE = 2 ** 20
DEFAULT_HASH_ALGORITHM = "md5"

T = TypeVar("T")
T_contra = TypeVar("T_contra", contravariant=True)

class Updatable(Protocol, Generic[T_contra]):
    def update(self, __data: T_contra, /): ...

def check_arg_type(args: Namespace, key: str, expected: Type[T] | str) -> T:
    try:
        value = args.__getattribute__(key)
    except AttributeError:
        raise Exception(f"Expected argument {key} in args namespace!")
    if isinstance(expected, str):
        value_class = value.__class__
        class_name = value_class.__name__
        if class_name != expected:
            raise Exception(f"Expected argument {key} to be of known type {expected}, but got {class_name}!")
    elif not isinstance(value, expected): 
        raise Exception(f"Expected argument {key} to be of type {expected}, but got {type(value).__name__}!")
    return value

def parse_args():
    parser = ArgumentParser("python -m hasher")
    if not DEFAULT_HASH_ALGORITHM in algorithms_available:
        raise Exception(f"Default hash algorithm {DEFAULT_HASH_ALGORITHM} is not available!")
    parser.add_argument("-a", type=str, choices=algorithms_available, default=DEFAULT_HASH_ALGORITHM, help="hash algorithm to use")
    parser.add_argument("file", type=FileType("rb"))
    return parser.parse_args()

def update(hasher: Updatable[bytes], file: IO[bytes], chunk_size: int = CHUNK_SIZE):
    while True:
        data = file.read(chunk_size)
        if not data: break
        hasher.update(data)

def main():
    args = parse_args()
    check_arg = partial(check_arg_type, args)
    algo = check_arg("a", str)
    file = check_arg("file", BufferedReader)
    hasher = new(algo)
    update(hasher, file)
    print(hasher.hexdigest())

if __name__ == '__main__':
    main()
