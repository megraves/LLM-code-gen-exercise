"""
Module containing various implementations of a function to return 
sorted unique elements from a list.
"""

# func3 and func5 require imports
from collections import OrderedDict
import itertools

def func1(l: list) -> list:
    """
    Return sorted unique elements using the most Pythonic way: 
    converting to a set for uniqueness, then sorting.
    Time Complexity: O(N log N) dominated by sorting.
    """
    # 1. Convert to set to get unique elements (O(N))
    # 2. Sort the unique elements (O(N log N))
    return sorted(set(l))

def func2(l: list) -> list:
    """
    Return sorted unique elements using a loop for manual uniqueness 
    checking followed by a final sort. This is generally the least 
    efficient method due to repeated 'in' checks.
    Time Complexity: O(N^2) for the uniqueness loop, then O(N log N) for sort.
    """
    unique_list = []
    for x in l:
        # The 'in' operator on a list is O(N) on average, making the loop O(N^2)
        if x not in unique_list:
            unique_list.append(x)
            
    # Final sort
    return sorted(unique_list)

def func3(l: list) -> list:
    """
    Return sorted unique elements using dict.fromkeys for fast uniqueness 
    extraction (maintaining insertion order), followed by sorting.
    Time Complexity: O(N) for dict creation, then O(N log N) for sort.
    """
    # dict.fromkeys leverages hash tables for O(1) average uniqueness check.
    # We convert to a list to extract the unique elements.
    unique_elements = list(dict.fromkeys(l)) 
    
    return sorted(unique_elements)

def func4(l: list) -> list:
    """
    Return sorted unique elements by sorting first, then iterating to check 
    for adjacent differences to identify duplicates. This avoids hash-based 
    structures (sets/dicts).
    Time Complexity: O(N log N) dominated by the initial sort.
    """
    if not l:
        return []

    # 1. Sort the list first (O(N log N)). This groups duplicates adjacently.
    s = sorted(l)
    unique_list = []
    
    # 2. Add the first element
    if s:
        unique_list.append(s[0])
    
    # 3. Iterate from the second element (O(N))
    for i in range(1, len(s)):
        # Only add the element if it's different from the one immediately before it
        if s[i] != s[i-1]:
            unique_list.append(s[i])
            
    # The result is already sorted
    return unique_list

def func5(l: list) -> list:
    """
    Return sorted unique elements using sorting combined with itertools.groupby.
    This is an elegant functional approach.
    Time Complexity: O(N log N) dominated by the initial sort.
    """
    # 1. Sort the list (O(N log N))
    sorted_l = sorted(l)
    
    # 2. Use groupby to cluster identical, adjacent elements. 
    # The list comprehension extracts the 'key' (the unique element) for each group.
    return [key for key, group in itertools.groupby(sorted_l)]


if __name__ == '__main__':
    # Example usage and testing
    test_list = [5, 3, 5, 2, 3, 3, 9, 0, 123, -1, 5]
    expected_result = [-1, 0, 2, 3, 5, 9, 123]

    print(f"Test List: {test_list}")
    print("-" * 30)

    results = {
        'func1': func1(test_list),
        'func2': func2(test_list),
        'func3': func3(test_list),
        'func4': func4(test_list),
        'func5': func5(test_list)
    }

    for name, result in results.items():
        is_correct = "CORRECT" if result == expected_result else "INCORRECT"
        print(f"{name}: {result} ({is_correct})")

cot_gemini = [func1, func2, func3, func4, func5]