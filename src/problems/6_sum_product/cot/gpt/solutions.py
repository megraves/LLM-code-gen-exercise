from typing import List, Tuple
import math
from functools import reduce
import operator

def func1(numbers: List[int]) -> Tuple[int, int]:
    """
    Single-pass loop. Explicitly handles empty list by initializing sum=0, prod=1.
    """
    total = 0
    prod = 1
    for x in numbers:
        total += x
        prod *= x
    return total, prod

def func2(numbers: List[int]) -> Tuple[int, int]:
    """
    Use built-ins: sum() and math.prod(). math.prod([]) == 1 so empty product OK.
    """
    return sum(numbers), math.prod(numbers)

def func3(numbers: List[int]) -> Tuple[int, int]:
    """
    Use reduce for the product and sum() for the sum.
    """
    total = sum(numbers)
    # reduce on empty sequence would raise; provide default 1
    if not numbers:
        prod = 1
    else:
        prod = reduce(operator.mul, numbers, 1)
    return total, prod

def func4(numbers: List[int]) -> Tuple[int, int]:
    """
    Recursive implementation with accumulators.
    Note: recursion depth limit may be hit for very large lists.
    """
    def _rec(i: int, s: int, p: int) -> Tuple[int, int]:
        if i >= len(numbers):
            return s, p
        return _rec(i + 1, s + numbers[i], p * numbers[i])
    return _rec(0, 0, 1)

def func5(numbers: List[int]) -> Tuple[int, int]:
    """
    Functional single-pass: update a (sum, prod) tuple per element.
    """
    s, p = 0, 1
    for x in numbers:
        s, p = s + x, p * x
    return s, p

funcs=[func1, func2, func3, func4, func5]
