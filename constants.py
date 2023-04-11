from typing import cast, NewType, Optional, Callable, overload, TypeVar, Union
from decouple import config

T = TypeVar("T")
V = TypeVar("V")
Sentinel = NewType("Sentinel", object)
_MISSING = cast(Sentinel, object())


@overload
def _get_config(search_path: str, cast: None = None, default: Union[V, Sentinel] = _MISSING) -> Union[str, V]:
    ...


@overload
def _get_config(search_path: str, cast: Callable[[str], T], default: Union[V, Sentinel] = _MISSING) -> Union[T, V]:
    ...


def _get_config(
        search_path: str,
        cast: Optional[Callable[[str], object]] = None,
        default: object = _MISSING,
) -> object:
    """Wrapper around decouple.config that can handle typing better."""
    if cast is None:
        cast = lambda x: x

    if default is not _MISSING:
        obj = config(search_path, cast=cast, default=default)
    else:
        obj = config(search_path, cast=cast)

    return obj


class Connection:
    """Config connection to database"""
    NAME = _get_config("NAME")
    USER = _get_config("USER")
    PASSWORD = _get_config("PASSWORD")
    HOST = _get_config("HOST")
    PORT = _get_config("PORT")


class DjangoSettings:
    """Django settings getting from .env"""
    SECRET_KEY = _get_config("SECRET_KEY")
    DEBUG = _get_config("DEBUG", cast=int, default=0)
