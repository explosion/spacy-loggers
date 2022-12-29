"""
Configuration utilities copied from spacy.util.
"""
from typing import Dict, Any, Tuple, Callable, Iterator, List, Optional, IO
import re

from spacy import Language


LoggerT = Callable[
    [Language, IO, IO],
    Tuple[Callable[[Optional[Dict[str, Any]]], None], Callable[[], None]],
]


def walk_dict(
    node: Dict[str, Any], parent: List[str] = []
) -> Iterator[Tuple[List[str], Any]]:
    """Walk a dict and yield the path and values of the leaves."""
    for key, value in node.items():
        key_parent = [*parent, key]
        if isinstance(value, dict):
            yield from walk_dict(value, key_parent)
        else:
            yield (key_parent, value)


def dot_to_dict(values: Dict[str, Any]) -> Dict[str, dict]:
    """Convert dot notation to a dict. For example: {"token.pos": True,
    "token._.xyz": True} becomes {"token": {"pos": True, "_": {"xyz": True }}}.

    values (Dict[str, Any]): The key/value pairs to convert.
    RETURNS (Dict[str, dict]): The converted values.
    """
    result = {}
    for key, value in values.items():
        path = result
        parts = key.lower().split(".")
        for i, item in enumerate(parts):
            is_last = i == len(parts) - 1
            path = path.setdefault(item, value if is_last else {})
    return result


def dict_to_dot(obj: Dict[str, dict]) -> Dict[str, Any]:
    """Convert dot notation to a dict. For example: {"token": {"pos": True,
    "_": {"xyz": True }}} becomes {"token.pos": True, "token._.xyz": True}.

    values (Dict[str, dict]): The dict to convert.
    RETURNS (Dict[str, Any]): The key/value pairs.
    """
    return {".".join(key): value for key, value in walk_dict(obj)}


def setup_custom_stats_matcher(
    regexps: Optional[List[str]] = None,
) -> Callable[[str], bool]:
    try:
        compiled = []
        if compiled is not None:
            for regex in regexps:
                compiled.append(re.compile(regex))
    except:
        raise ValueError(
            f"Regular expression `{regex}` couldn't be compiled for logger stats matcher"
        )

    def is_match(string: str) -> bool:
        for regex in compiled:
            if regex.match(string):
                return True
        return False

    return is_match
