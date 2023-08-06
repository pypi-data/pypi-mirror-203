from typing import (
    TypeVar,
    NoReturn
)

TValue = TypeVar("TValue")

class ReadOnlyLib:
    """
    This class makes any module attributes read only.
    """

    def __init__(self, lib):
        self.__dict__['_lib'] = lib
        self.__dict__.update(lib.__dict__)

    @property
    def _lib(self):
        return self._lib

    def __getattr__(self, name: str):
        return getattr(self._lib, name)

    def __setattr__(self, name: str, value: TValue) -> NoReturn:
        raise AttributeError("can't set attribute")

readonly = ReadOnlyLib

__all__ = [
    "readonly",
]
