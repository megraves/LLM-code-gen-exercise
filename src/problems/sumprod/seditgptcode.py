from typing import List, Tuple
from functools import reduce
import operator
import math
import numpy as np

# ---------------------------
# func1: iterative loop
# ---------------------------
def func1(numbers: List[int]) -> Tuple[int, int]:
    total = 0
    product = 1
    for num in numbers:
        total += num
        product *= num
    return (total, product)

# ---------------------------
# func2: built-in sum and math.prod
# ---------------------------
def func2(numbers: List[int]) -> Tuple[int, int]:
    return (sum(numbers), math.prod(numbers) if numbers else 1)

# ---------------------------
# func3: functools.reduce
# ---------------------------
def func3(numbers: List[int]) -> Tuple[int, int]:
    total = sum(numbers)
    product = reduce(operator.mul, numbers, 1)  # 1 is initial for empty list
    return (total, product)

# ---------------------------
# func4: recursive
# ---------------------------
def func4(numbers: List[int]) -> Tuple[int, int]:
    if not numbers:
        return (0, 1)
    s, p = func4(numbers[1:])
    return (numbers[0] + s, numbers[0] * p)

# ---------------------------
# func5: numpy
# ---------------------------
def func5(numbers: List[int]) -> Tuple[int, int]:
    if not numbers:
        return (0, 1)
    arr = np.array(numbers)
    return (int(arr.sum()), int(arr.prod()))

sedit_gpt = [func1, func2, func3, func4, func5]