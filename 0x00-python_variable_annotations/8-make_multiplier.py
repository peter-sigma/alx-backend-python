#!/usr/bin/env python3
"""function make_multiplier"""
from typing import Callable


def make_multiplier(multiplier: float) -> Callable[[float], float]:
    """function: make_multiplier
    Args:
    multiplier (float) : argument to multiply
    return:
    a function that multiplies a float by multiplier.
    """

    def fn(n: float) -> float:
        """
        Multiply a float by a multiplier
        
        """
        return n * multiplier

    return fn
