from typing import List
import numpy as np # Required for func4

def func1(numbers: List[float]) -> List[float]:
    """
    func1: Basic Iterative Approach.
    
    Finds min/max/range, handles the zero-range edge case, and uses a standard 
    'for' loop to calculate the scaled values.
    """
    min_val = min(numbers)
    max_val = max(numbers)
    data_range = max_val - min_val

    # Edge case: all numbers are the same
    if data_range == 0:
        return [0.0] * len(numbers)

    scaled_numbers = []
    for num in numbers:
        # Formula: (x - min) / range
        scaled_num = (num - min_val) / data_range
        scaled_numbers.append(scaled_num)

    return scaled_numbers

# ----------------------------------------------------------------------

def func2(numbers: List[float]) -> List[float]:
    """
    func2: List Comprehension Approach (The most 'Pythonic' way).
    
    Similar logic to func1 but uses a concise list comprehension for the scaling.
    """
    min_val = min(numbers)
    max_val = max(numbers)
    data_range = max_val - min_val

    # Edge case: zero range
    if data_range == 0:
        return [0.0] * len(numbers)

    # Use a list comprehension to calculate all scaled values in one line
    return [(num - min_val) / data_range for num in numbers]

# ----------------------------------------------------------------------

def func3(numbers: List[float]) -> List[float]:
    """
    func3: Map and Lambda Approach.
    
    Uses the built-in map() function and a lambda function to apply the scaling,
    which is then converted back to a list.
    """
    min_val = min(numbers)
    max_val = max(numbers)
    data_range = max_val - min_val

    # Edge case: zero range
    if data_range == 0:
        return [0.0] * len(numbers)

    # Use map with a lambda function for the scaling
    return list(map(lambda x: (x - min_val) / data_range, numbers))

# ----------------------------------------------------------------------

def func4(numbers: List[float]) -> List[float]:
    """
    func4: NumPy Vectorized Approach (Requires NumPy).
    
    The most performant approach for large datasets, utilizing NumPy's array 
    and vectorized operations (`np.ptp` for range).
    """
    # Convert to NumPy array
    np_array = np.array(numbers, dtype=float)

    min_val = np_array.min()
    # np.ptp() calculates the peak-to-peak range (max - min)
    data_range = np.ptp(np_array)

    # Edge case: zero range
    if data_range == 0:
        return [0.0] * len(numbers)

    # Apply the scaling formula using vectorized operations
    scaled_array = (np_array - min_val) / data_range

    # Convert the result back to a standard Python list
    return scaled_array.tolist()

# ----------------------------------------------------------------------

def func5(numbers: List[float]) -> List[float]:
    """
    func5: Pre-calculated Constant Multiplier Approach.
    
    Calculates the inverse of the range (1/R) once, replacing the division 
    inside the loop/comprehension with a multiplication for a minor optimization.
    """
    min_val = min(numbers)
    max_val = max(numbers)
    data_range = max_val - min_val

    # Edge case: zero range
    if data_range == 0:
        return [0.0] * len(numbers)

    # Optimization: Calculate the constant multiplier (1 / range) once
    inverse_range = 1.0 / data_range

    # Use a list comprehension with the pre-calculated multiplier: (x - min) * (1/R)
    return [(num - min_val) * inverse_range for num in numbers]


# Example usage (Testing the expected output):
# test_data = [1.0, 2.0, 3.0, 4.0, 5.0]
# print(f"Func 1: {func1(test_data)}")
# print(f"Func 2: {func2(test_data)}")
# print(f"Func 3: {func3(test_data)}")
# print(f"Func 4: {func4(test_data)}")
# print(f"Func 5: {func5(test_data)}")

funcs = [func1, func2, func3, func4, func5]