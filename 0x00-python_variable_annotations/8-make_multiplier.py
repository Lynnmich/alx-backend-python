#!/usr/bin/env python3
"""function make_multiplier that takes an argument and returns a function"""
from typing import Callable


def make_multiplier(multiplier: float) -> Callable[[float], float]:
    """returns multiplied value"""

    def function_multiplier(number: float) -> float:
        "multiplied by a number"""
        return multiplier * number

    return function_multiplier
