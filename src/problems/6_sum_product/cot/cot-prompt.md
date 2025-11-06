Give 5 different solutions for this problem labeled func1 through func5. From the given programming specification, reason step by step in a chain of thought before giving your answer. The programming specification is

from typing import List, Tuple


def sum_product(numbers: List[int]) -> Tuple[int, int]:
""" For a given list of integers, return a tuple consisting of a sum and a product of all the integers in a list.
Empty sum should be equal to 0 and empty product should be equal to 1.
>>> sum_product([])
(0, 1)
>>> sum_product([1, 2, 3, 4])
(10, 24)
"""