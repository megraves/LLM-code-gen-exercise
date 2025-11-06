from typing import List
import numpy as np

def func1(numbers: List[float]) -> List[float]:
    """Rescale numbers to [0, 1] using list comprehension."""
    min_val = min(numbers)
    max_val = max(numbers)
    range_val = max_val - min_val
    return [(x - min_val) / range_val for x in numbers]

def func2(numbers: List[float]) -> List[float]:
    """Rescale numbers to [0, 1] using a traditional for loop."""
    min_val = min(numbers)
    max_val = max(numbers)
    range_val = max_val - min_val
    result = []
    for x in numbers:
        result.append((x - min_val) / range_val)
    return result

def func3(numbers: List[float]) -> List[float]:
    """Rescale numbers to [0, 1] with handling for identical numbers."""
    min_val = min(numbers)
    max_val = max(numbers)
    range_val = max_val - min_val
    if range_val == 0:  # all numbers identical
        return [0.0 for _ in numbers]
    return [(x - min_val) / range_val for x in numbers]

def func4(numbers: List[float]) -> List[float]:
    """Rescale numbers to [0, 1] using map and lambda."""
    min_val = min(numbers)
    max_val = max(numbers)
    range_val = max_val - min_val
    return list(map(lambda x: (x - min_val) / range_val, numbers))

def func5(numbers: List[float]) -> List[float]:
    """Rescale numbers to [0, 1] using numpy (vectorized)."""
    arr = np.array(numbers, dtype=float)
    min_val = arr.min()
    max_val = arr.max()
    range_val = max_val - min_val
    if range_val == 0:
        return [0.0] * len(numbers)
    return ((arr - min_val) / range_val).tolist()

funcs = [func1, func2, func3, func4, func5]