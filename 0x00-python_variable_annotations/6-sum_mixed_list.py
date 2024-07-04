#!/usr/bin/env python3
"""
calculate the sum of mixed list ie, int and floats
"""
from typing import List, Union


def sum_mixed_list(mxd_lst: List[Union[int, float]]) -> float:
    """Sum float and int

    Args:
        mxd_lst (List[float, int]): List of floats and ints

    Return:
        (float): sum of the list
    """
    return float(sum(mxd_lst))
