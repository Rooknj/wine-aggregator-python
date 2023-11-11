import textwrap
from typing import Any


def safeget(dct: dict, *keys: str | int) -> Any:
    for key in keys:
        try:
            dct = dct[key]
        except KeyError:
            return None
    return dct


def trim_indent(fstring: str):
    string_without_indent = textwrap.dedent(fstring)
    # if string_without_indent.startswith("\n"):
    #     return string_without_indent[1:]
    return string_without_indent.strip()
