#!/usr/bin/env python3
"""Function that takes arguments and returns a tuple"""


def to_kv(k: str, v: Union[int, float]) -> tuple[str, float]:
    """returnsa string and a float"""
    return k, v**2
