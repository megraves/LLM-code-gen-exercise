from typing import List, Tuple
import math
from functools import reduce
import operator

# --- func1: Standard Loop ---
def func1(numbers: List[int]) -> Tuple[int, int]:
    """
    Uses a standard for loop to calculate both sum and product.
    Handles empty list: sum starts at 0, product starts at 1.
    """
    current_sum = 0
    current_product = 1
    for num in numbers:
        current_sum += num
        current_product *= num
    return (current_sum, current_product)

# --- func2: Using sum() and a Loop for Product ---
def func2(numbers: List[int]) -> Tuple[int, int]:
    """
    Uses built-in sum() for the sum and a loop for the product.
    """
    total_sum = sum(numbers)  # sum([]) == 0
    total_product = 1
    for num in numbers:
        total_product *= num
    return (total_sum, total_product)

# --- func3: Using functools.reduce ---
def func3(numbers: List[int]) -> Tuple[int, int]:
    """
    Uses functools.reduce with initial values (0 for sum, 1 for product).
    """
    # Initial value 0 ensures sum([]) == 0
    total_sum = reduce(operator.add, numbers, 0)

    # Initial value 1 ensures product([]) == 1
    total_product = reduce(operator.mul, numbers, 1)

    return (total_sum, total_product)

# --- func4: Using sum() and math.prod() (Python 3.8+) ---
def func4(numbers: List[int]) -> Tuple[int, int]:
    """
    Uses the built-in functions sum() and math.prod().
    """
    total_sum = sum(numbers)        # sum([]) == 0
    total_product = math.prod(numbers) # math.prod([]) == 1
    return (total_sum, total_product)

# --- func5: Recursive Solution ---
def func5(numbers: List[int]) -> Tuple[int, int]:
    """
    A recursive implementation.
    """
    # Base case: empty list returns (0, 1)
    if not numbers:
        return (0, 1)

    # Recursive step
    first_num = numbers[0]
    rest_sum, rest_product = func5(numbers[1:])

    total_sum = first_num + rest_sum
    total_product = first_num * rest_product

    return (total_sum, total_product)

sedit_gemini = [func1, func2, func3, func4, func5]