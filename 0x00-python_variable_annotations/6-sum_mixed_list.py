#!/usr/bin/env python3
""" function takes a list mxd_lst of integers and floats & returns the sum"""
from typing import List, Union


def sum_mixed_list(mxd_lst: List[Union[int, float]]) -> float:
    """returns sum of mixed list"""
    return sum(mxd_lst)
