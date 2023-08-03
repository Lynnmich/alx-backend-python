#!/usr/bin/env python3
"""function returns values with appropriate types"""
from typing import Iterable, List, Sequence, Tuple


def element_length(lst: Iterable[Sequence]) -> List[Tuple[Sequence, int]]:
    """returns a list of tuples with length of each"""
    return [(i, len(i)) for i in lst]
