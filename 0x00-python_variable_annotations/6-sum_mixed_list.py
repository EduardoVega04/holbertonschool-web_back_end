#!/usr/bin/env python3
"""Type-annotated function sum_mixed_list which takes a
list mxd_lst of integers and floats and returns their sum as a float"""

from typing import List


def sum_mixed_list(mxd_lst: List[int]) -> float:
    """Returns the sum of the list as a float"""
    total: float = 0.0
    for i in mxd_lst:
        total += i
    return total
