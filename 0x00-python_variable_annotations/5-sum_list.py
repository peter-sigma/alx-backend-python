#!/usr/bin/env python3
from typing import List
"""
calculate the sum of the floats in a list
"""


def sum_list(input_list: List[float]) -> float:
    """Sum list of float in the list

    Args:
        input_list (List[float]): List of float

    Return
        (float): sum of all element
    """
    sum = 0
    for item in input_list:
        sum += item

    return sum
