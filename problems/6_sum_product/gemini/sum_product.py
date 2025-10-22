# Generated from Gemini using C-o-T
from typing import List, Tuple


def sum_product(numbers: List[int]) -> Tuple[int, int]:
    """ For a given list of integers, return a tuple consisting of a 
    sum and a product of all the integers in a list.
    Empty sum should be equal to 0 and empty product should be equal to 1.
    >>> sum_product([])
    (0, 1)
    >>> sum_product([1, 2, 3, 4])
    (10, 24)
    """
    
    # Initialize the sum to 0 (the additive identity).
    # This ensures that if the list is empty, the sum is 0.
    total_sum = 0
    
    # Initialize the product to 1 (the multiplicative identity).
    # This ensures that if the list is empty, the product is 1.
    total_product = 1
    
    # Iterate through each number in the list
    for num in numbers:
        # Accumulate the sum
        total_sum += num
        # Accumulate the product
        total_product *= num
        
    # Return the final accumulated values as a tuple
    return (total_sum, total_product)