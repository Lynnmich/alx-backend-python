#!/usr/bin/env python3
"""Function that takes arguments and returns a tuple"""
from typing import List, Union, Tuple


def to_kv(k: str, v: Union[int, float]) -> Tuple[str, float]:
    """returns a string and a float"""
    return k, v**2
