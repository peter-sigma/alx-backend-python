#!/usr/bin/env python3
"""
iterable object
"""
from typing import Sequence, Iterable, List, Tuple


def element_length(lst: Iterable[Sequence]) -> List[Tuple[Sequence, int]]:
    """
    Element length
    """
    return [(i, len(i)) for i in lst]
