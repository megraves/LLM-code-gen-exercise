from typing import List
import numpy as np

def func1(numbers: List[float]) -> List[float]:
    """Rescale numbers to unit interval using list comprehension"""
    min_val = min(numbers)
    max_val = max(numbers)
    range_val = max_val - min_val
    if range_val == 0:
        return [0.0 for _ in numbers]
    return [(x - min_val) / range_val for x in numbers]

def func2(numbers: List[float]) -> List[float]:
    """Rescale numbers to unit interval using map"""
    min_val = min(numbers)
    max_val = max(numbers)
    range_val = max_val - min_val
    if range_val == 0:
        return [0.0] * len(numbers)
    return list(map(lambda x: (x - min_val) / range_val, numbers))

def func3(numbers: List[float]) -> List[float]:
    """Rescale numbers to unit interval using numpy"""
    arr = np.array(numbers, dtype=float)
    min_val = arr.min()
    max_val = arr.max()
    range_val = max_val - min_val
    if range_val == 0:
        return [0.0] * len(numbers)
    scaled = (arr - min_val) / range_val
    return scaled.tolist()

def func4(numbers: List[float]) -> List[float]:
    """Rescale numbers to unit interval using an iterative approach"""
    min_val = min(numbers)
    max_val = max(numbers)
    range_val = max_val - min_val
    result = []
    if range_val == 0:
        return [0.0] * len(numbers)
    for x in numbers:
        result.append((x - min_val) / range_val)
    return result

def func5(numbers: List[float]) -> List[float]:
    """Rescale numbers to unit interval using in-place list modification"""
    min_val = min(numbers)
    max_val = max(numbers)
    range_val = max_val - min_val
    scaled_numbers = numbers.copy()
    if range_val == 0:
        return [0.0] * len(numbers)
    for i, x in enumerate(numbers):
        scaled_numbers[i] = (x - min_val) / range_val
    return scaled_numbers

scot_gpt = [func1, func2, func3, func4, func5]