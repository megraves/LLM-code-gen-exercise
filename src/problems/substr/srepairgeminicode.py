# Generated from gemini
import re

# --- Solution 1: Pure Iterative Loop with Slicing ---
def func1(string: str, substring: str) -> int:
    """ 
    Find how many times a given substring can be found in the original string. 
    Count overlapping cases using an iterative loop and string slicing.

    >>> func1('', 'a')
    0
    >>> func1('aaa', 'a')
    3
    >>> func1('aaaa', 'aa')
    3
    """
    if not substring:
        return 0
    
    count = 0
    sub_len = len(substring)
    str_len = len(string)
    
    # The loop iterates through every possible starting position for the substring.
    # We stop when the remaining length is less than the substring's length.
    for i in range(str_len - sub_len + 1):
        if string[i:i + sub_len] == substring:
            count += 1
            
    return count

# --- Solution 2: Using str.find() in a While Loop ---
def func2(string: str, substring: str) -> int:
    """ 
    Find how many times a given substring can be found in the original string. 
    Count overlapping cases by using str.find() and advancing the search 
    position by only one character on a match.
    """
    if not substring:
        return 0
        
    count = 0
    start_index = 0
    
    while True:
        # Find the next occurrence starting from the current start_index
        index = string.find(substring, start_index)
        
        if index == -1:
            # No more occurrences found
            break
        
        count += 1
        
        # CRUCIAL FOR OVERLAP: Advance the search starting position by 1 
        # (not by len(substring)), which allows the next search to start 
        # immediately after the character where the current match began.
        start_index = index + 1
        
    return count


# --- Solution 3: List Comprehension and Sum ---
def func3(string: str, substring: str) -> int:
    """ 
    Find how many times a given substring can be found in the original string. 
    Count overlapping cases using a concise list comprehension and sum approach.
    """
    if not substring:
        return 0
        
    sub_len = len(substring)
    
    # Generate 1 for every match found by slicing and comparison, and sum the results.
    return sum(
        1 for i in range(len(string) - sub_len + 1) 
        if string[i:i + sub_len] == substring
    )


# --- Solution 4: Regular Expressions with Positive Lookahead ---
def func4(string: str, substring: str) -> int:
    """ 
    Find how many times a given substring can be found in the original string. 
    Count overlapping cases using Python's 're' module with a positive lookahead assertion.
    """
    if not substring:
        return 0
    
    # 1. Escape the substring to handle potential regex special characters (like '.', '*', etc.)
    escaped_substring = re.escape(substring)
    
    # 2. Use positive lookahead `(?=...)`
    # This assertion finds an empty string match (zero width) only if it is 
    # immediately followed by the substring pattern. Because the match is zero-width, 
    # the regex engine can immediately check for the next match at the very next character, 
    # ensuring overlaps are counted.
    pattern = f'(?={escaped_substring})'
    
    # len() of the list of all found matches (the zero-width positions) is the count.
    return len(re.findall(pattern, string))


# --- Solution 5: Recursive Implementation ---
def func5(string: str, substring: str) -> int:
    """ 
    Find how many times a given substring can be found in the original string. 
    Count overlapping cases using a recursive function that checks for a match 
    at the current position and then calls itself for the next character.
    """
    if not substring:
        return 0
    
    sub_len = len(substring)
    str_len = len(string)
    
    def recursive_count(index: int) -> int:
        # Base case: if the starting index is past the point where a full 
        # substring can fit, return 0.
        if index > str_len - sub_len:
            return 0
        
        # Check if the substring is present starting at the current index
        is_match = (string[index:index + sub_len] == substring)
        
        # Recursive Step: 
        # Add the current match (1 or 0) to the count from the NEXT position (index + 1)
        # Moving to index + 1 ensures the overlapping count.
        return (1 if is_match else 0) + recursive_count(index + 1)

    # Start the recursion from the beginning of the string
    return recursive_count(0)

srepair_gemini = [func1, func2, func3, func4, func5]