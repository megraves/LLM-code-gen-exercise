from typing import List, Tuple
from functools import reduce
import operator
import math # Not used, but often useful for math ops

# --- Solution 1: Standard 'for' Loop Iteration ---

def func1(numbers: List[int]) -> Tuple[int, int]:
    """Uses a single standard 'for' loop to calculate both sum and product."""
    total_sum = 0
    total_product = 1
    
    for number in numbers:
        total_sum += number
        total_product *= number
        
    return (total_sum, total_product)


# --- Solution 2: Built-in 'sum()' and Product Loop ---

def func2(numbers: List[int]) -> Tuple[int, int]:
    """Uses the built-in sum() function for the sum and a 'for' loop for the product."""
    
    # Sum is calculated concisely
    total_sum = sum(numbers)
    
    # Product must be calculated via iteration
    total_product = 1
    for number in numbers:
        total_product *= number
        
    return (total_sum, total_product)


# --- Solution 3: Using functools.reduce ---

def func3(numbers: List[int]) -> Tuple[int, int]:
    """Uses functools.reduce with operator functions for both sum and product."""
    
    # The '0' and '1' arguments are the initial values, handling the empty list case.
    total_sum = reduce(operator.add, numbers, 0)
    total_product = reduce(operator.mul, numbers, 1)
        
    return (total_sum, total_product)


# --- Solution 4: Recursive Approach ---

def func4(numbers: List[int]) -> Tuple[int, int]:
    """Uses a recursive definition to break the problem into smaller sub-problems."""
    
    # Base Case: Empty list returns (0, 1)
    if not numbers:
        return (0, 1)
    
    # Recursive Step: Get the sum/product of the rest of the list
    head = numbers[0]
    tail_sum, tail_product = func4(numbers[1:])
    
    # Combine the head with the recursive result
    current_sum = head + tail_sum
    current_product = head * tail_product
    
    return (current_sum, current_product)


# --- Solution 5: Explicit Length Check and Standard Loop ---

def func5(numbers: List[int]) -> Tuple[int, int]:
    """Uses built-in sum() and includes an explicit check for an empty list before calculating product."""
    
    total_sum = sum(numbers)
    
    if len(numbers) == 0:
        # Explicitly handles the product base case when sum() already handled the sum base case
        total_product = 1
    else:
        # Standard product calculation loop for non-empty lists
        total_product = 1
        for number in numbers:
            total_product *= number
            
    return (total_sum, total_product)

funcs = [func1, func2, func3, func4, func5]