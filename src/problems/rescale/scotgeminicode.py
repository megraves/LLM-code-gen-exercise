from typing import List

def func1(numbers: List[float]) -> List[float]:
    """Simple iterative solution."""
    min_val = min(numbers)
    max_val = max(numbers)
    data_range = max_val - min_val

    if data_range == 0.0:
        return [0.0] * len(numbers)

    rescaled_list = []
    for x in numbers:
        rescaled_x = (x - min_val) / data_range
        rescaled_list.append(rescaled_x)

    return rescaled_list

# -------------------------------------------------------------------------
# func2: List Comprehension (The Pythonic way)
# -------------------------------------------------------------------------
def func2(numbers: List[float]) -> List[float]:
    """Concise solution using list comprehension."""
    min_val = min(numbers)
    max_val = max(numbers)
    data_range = max_val - min_val

    if data_range == 0.0:
        return [0.0] * len(numbers)

    return [(x - min_val) / data_range for x in numbers]

# -------------------------------------------------------------------------
# func3: Using the map Function
# -------------------------------------------------------------------------
def func3(numbers: List[float]) -> List[float]:
    """Functional programming approach using map and lambda."""
    min_val = min(numbers)
    max_val = max(numbers)
    data_range = max_val - min_val

    if data_range == 0.0:
        return [0.0] * len(numbers)

    transform = lambda x: (x - min_val) / data_range
    
    return list(map(transform, numbers))

# -------------------------------------------------------------------------
# func4: Generator Expression (Memory-Efficient for large lists)
# -------------------------------------------------------------------------
def func4(numbers: List[float]) -> List[float]:
    """Uses a generator expression for lazy evaluation before list creation."""
    min_val = min(numbers)
    max_val = max(numbers)
    data_range = max_val - min_val

    if data_range == 0.0:
        return [0.0] * len(numbers)

    # Generator yields values one by one, then list() consumes it
    generator = ((x - min_val) / data_range for x in numbers)
    
    return list(generator)

# -------------------------------------------------------------------------
# func5: Two-Pass Loop (Manual Min/Max Calculation)
# -------------------------------------------------------------------------
def func5(numbers: List[float]) -> List[float]:
    """Manual two-pass approach (first pass for min/max, second for transform)."""
    # Pass 1: Manually find min/max
    min_val = numbers[0]
    max_val = numbers[0]
    for x in numbers[1:]:
        if x < min_val:
            min_val = x
        if x > max_val:
            max_val = x

    data_range = max_val - min_val

    if data_range == 0.0:
        return [0.0] * len(numbers)

    # Pass 2: Apply transformation
    rescaled_list = []
    for x in numbers:
        rescaled_x = (x - min_val) / data_range
        rescaled_list.append(rescaled_x)

    return rescaled_list


scot_gemini = [func1, func2, func3, func4, func5]