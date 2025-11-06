import string

def func1(s: str) -> str:
    """
    Solution 1: Using the built-in string method `swapcase()`.
    This is the most direct, pythonic, and efficient approach.
    >>> func1('Hello World 123!')
    'hELLO wORLD 123!'
    """
    return s.swapcase()

def func2(s: str) -> str:
    """
    Solution 2: Using a List Comprehension with Conditional Logic.
    Iterates through the string and explicitly checks the case of each character,
    using string methods (.islower(), .upper(), .lower()).
    >>> func2('Hello World 123!')
    'hELLO wORLD 123!'
    """
    return "".join([
        char.upper() if char.islower()
        else char.lower() if char.isupper()
        else char
        for char in s
    ])

def func3(s: str) -> str:
    """
    Solution 3: Using `str.maketrans()` and `str.translate()`.
    This creates a highly optimized mapping table to swap all lowercase characters
    with their uppercase counterparts and vice versa in a single pass.
    This is very efficient for large strings.
    >>> func3('Hello World 123!')
    'hELLO wORLD 123!'
    """
    # Create the mapping: abc... -> ABC... and ABC... -> abc...
    lower_to_upper = string.ascii_lowercase
    upper_to_lower = string.ascii_uppercase
    
    # map_table maps all characters to their new case
    map_table = str.maketrans(lower_to_upper + upper_to_lower, upper_to_lower + lower_to_upper)
    
    return s.translate(map_table)

def func4(s: str) -> str:
    """
    Solution 4: Using `map()` with a Lambda Function.
    A functional approach that defines the case-flipping logic in an anonymous
    lambda function and applies it across the entire string using map().
    >>> func4('Hello World 123!')
    'hELLO wORLD 123!'
    """
    
    # Lambda implements the conditional case flip logic
    flip_logic = lambda char: (
        char.upper() if char.islower()
        else char.lower() if char.isupper()
        else char
    )
    
    # map() applies the lambda to every character; ''.join() reconstructs the string
    return "".join(map(flip_logic, s))

def func5(s: str) -> str:
    """
    Solution 5: Using Character ASCII/Unicode Codes (`ord` and `chr`).
    This demonstrates manipulating the raw character codes. For standard ASCII,
    the difference between an upper and lower case letter is 32 (e.g., ord('A')=65, ord('a')=97).
    This approach is explicit but less robust for full Unicode than methods relying on .islower().
    >>> func5('Hello World 123!')
    'hELLO wORLD 123!'
    """
    result = []
    for char in s:
        code = ord(char)
        if 'a' <= char <= 'z':
            # Lowercase to Uppercase: subtract 32
            result.append(chr(code - 32))
        elif 'A' <= char <= 'Z':
            # Uppercase to Lowercase: add 32
            result.append(chr(code + 32))
        else:
            # Keep non-alphabetic characters as is
            result.append(char)
    return "".join(result)


splan_gemini = [func1, func2, func3, func4, func5]