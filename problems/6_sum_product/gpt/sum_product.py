# Generated from GPT-4
from typing import List, Tuple

def sum_product(numbers: List[int]) -> Tuple[int, int]:
    """
    For a given list of integers, return a tuple consisting of a sum and a product
    of all the integers in the list. Empty sum == 0 and empty product == 1.

    Examples:
    >>> sum_product([])
    (0, 1)
    >>> sum_product([1, 2, 3, 4])
    (10, 24)
    """
    s = 0
    p = 1
    for n in numbers:
        s += n
        p *= n
    return s, p

# quick manual tests
if __name__ == "__main__":
    print(sum_product([]))            # (0, 1)
    print(sum_product([1, 2, 3, 4]))  # (10, 24)
    print(sum_product([0, 5, -2]))    # (3, 0)
