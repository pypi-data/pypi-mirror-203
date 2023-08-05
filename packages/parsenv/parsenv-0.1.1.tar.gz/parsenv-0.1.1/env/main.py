from .core import get_var, DT, UNDEFINED
from .parsers import parse_ints, parse_strs


def get(key: str, default: DT = UNDEFINED) -> str | DT:
    return get_var(key, default)


def get_int(key: str, default: DT = UNDEFINED) -> int | DT:
    return get_var(key, default, int)


def get_strs(key: str, default: DT = UNDEFINED) -> list[str] | DT:
    return get_var(key, default, parse_strs)


def get_ints(key: str, default: DT = UNDEFINED) -> list[int] | DT:
    return get_var(key, default, parse_ints)
