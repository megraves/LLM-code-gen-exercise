import re
from typing import List, Tuple

# --- Problem Definition ---
# Find how many times a given substring can be found in the original string,
# including overlapping cases (e.g., 'aaaa' and 'aa' should yield 3).

# --- Solution 1: Basic Sliding Window (Iterative Loop) ---
def func1(string: str, substring: str) -> int:
    """
    Counts occurrences using a traditional for loop and string slicing.
    This explicitly checks every possible starting position for a match.
    """
    if not substring:
        return 0
    
    count = 0
    sub_len = len(substring)
    str_len = len(string)
    
    # We iterate up to the last possible starting index for the substring
    # (i.e., str_len - sub_len). This ensures we check overlapping cases.
    for i in range(str_len - sub_len + 1):
        # Check if the slice starting at i matches the substring
        if string[i:i + sub_len] == substring:
            count += 1
            
    return count

# --- Solution 2: Iterative str.find() with +1 offset ---
def func2(string: str, substring: str) -> int:
    """
    Counts occurrences using the built-in str.find() method in a while loop.
    Crucially, the search index is advanced by only 1 after a match is found
    to ensure overlapping matches are detected.
    """
    if not substring:
        return 0
        
    count = 0
    start_index = 0
    
    while True:
        # Use find() to locate the next occurrence, starting from start_index
        found_index = string.find(substring, start_index)
        
        if found_index != -1:
            # A match was found. Increment the count.
            count += 1
            # Advance the starting index by only 1 position.
            # This allows the next search to overlap with the current match.
            start_index = found_index + 1
        else:
            # No more matches found. Exit the loop.
            break
            
    return count

# --- Solution 3: Generator Expression (Functional Style) ---
def func3(string: str, substring: str) -> int:
    """
    A concise, functional Pythonic approach using a generator expression 
    inside the sum() function, checking every possible starting index.
    """
    if not substring:
        return 0

    sub_len = len(substring)
    str_len = len(string)

    # Generate 1 for every index 'i' where the slice starting at 'i' 
    # matches the substring, and then sum those 1s.
    return sum(
        1 
        for i in range(str_len - sub_len + 1)
        if string[i:i + sub_len] == substring
    )

# --- Solution 4: Regular Expressions with Lookahead ---
def func4(string: str, substring: str) -> int:
    """
    Uses the 're' module with a positive lookahead assertion (?=...)
    to find matches without consuming characters, which is necessary for overlaps.
    """
    if not substring:
        return 0
    
    # Escape the substring to handle special regex characters if they exist
    escaped_substring = re.escape(substring)
    
    # The pattern uses a positive lookahead: (?=...). 
    # This checks for the substring but doesn't include it in the match, 
    # allowing the next search to start from the current position + 1 implicitly.
    pattern = r'(?={})'.format(escaped_substring)
    
    # re.findall returns a list of all non-overlapping matches found for the pattern.
    # Since the pattern is non-consuming, it effectively counts all overlaps.
    matches = re.findall(pattern, string)
    
    return len(matches)

# --- Solution 5: Recursion ---
def func5(string: str, substring: str) -> int:
    """
    Counts occurrences using a recursive function. It checks for a match 
    at the start of the current string slice and then recurses on string[1:]
    to always allow for overlaps.
    """
    if not substring:
        return 0

    sub_len = len(substring)
    
    # Base case: If the remaining string is shorter than the substring, no more matches possible.
    if len(string) < sub_len:
        return 0
        
    count = 0
    
    # Check for a match at the very beginning of the current string slice
    if string.startswith(substring):
        count = 1
        
    # Recursive step: Always call the function on the string starting from the next character (string[1:]).
    # This is what ensures overlapping is counted (e.g., check at index 0, then index 1, then index 2, etc.)
    return count + func5(string[1:], substring)

funcs = [func1, func2, func3, func4, func5]