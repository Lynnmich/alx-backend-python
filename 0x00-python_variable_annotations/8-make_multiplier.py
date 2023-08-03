#!/usr/bin/env python3
"""function make_multiplier that takes an argument and returns a function"""
from typing import Callable

def make_multiplier(multiplier: float) -> Callable[[float], float]:
    def function_multiplier(number: float) -> float:
        return multiplier * number
    return function_multiplier

