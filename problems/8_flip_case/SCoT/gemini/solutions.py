import re
# from typing import str

# --- Solution 1: Using the built-in swapcase() method (Most Idiomatic) ---
def func1(string: str) -> str:
    """
    Flips the case using the string's built-in swapcase() method.
    >>> func1('Hello World 123')
    'hELLO wORLD 123'
    """
    return string.swapcase()

# --- Solution 2: Using a Generator Expression and Ternary Operator (Pythonic Conditional) ---
def func2(string: str) -> str:
    """
    Flips the case using a generator expression, ternary conditional logic,
    and str.join(). This is highly efficient.
    >>> func2('PyThOn3.8')
    'pYtHoN3.8'
    """
    return "".join(c.upper() if c.islower() else c.lower() for c in string)

# --- Solution 3: Using a Traditional For Loop and List Append (Procedural) ---
def func3(string: str) -> str:
    """
    Flips the case using a traditional for loop, explicit checks (islower/isupper),
    and building the result via list append/join for efficiency.
    >>> func3('AlphaBetaGamma')
    'aLPHAbETAgAMMA'
    """
    result = []
    for char in string:
        # Check if it's lowercase
        if char.islower():
            result.append(char.upper())
        # Check if it's uppercase
        elif char.isupper():
            result.append(char.lower())
        # If it's not a letter (e.g., space, number, punctuation), keep it as is
        else:
            result.append(char)
    
    return "".join(result)

# --- Solution 4: Using map() and ASCII/Unicode Code Manipulation (Numeric) ---
def func4(string: str) -> str:
    """
    Flips the case by manipulating the character's ASCII/Unicode code.
    Lowercase and uppercase letters differ by 32.
    >>> func4('aBcDeFg 9!')
    'AbCdEfG 9!'
    """
    def toggle_case_by_code(char: str) -> str:
        code = ord(char)
        # Check for lowercase (97='a' to 122='z')
        if 97 <= code <= 122:
            return chr(code - 32) # Convert to uppercase
        # Check for uppercase (65='A' to 90='Z')
        elif 65 <= code <= 90:
            return chr(code + 32) # Convert to lowercase
        
        # Return non-alphabetic characters as is
        return char

    # Apply the helper function to every character and join
    return "".join(map(toggle_case_by_code, string))

# --- Solution 5: Using Regular Expression Substitution (Regex) ---
def func5(string: str) -> str:
    """
    Flips the case using re.sub() with a custom replacement function to
    target only alphabetic characters.
    >>> func5('Test_String_1')
    'tEST_sTRING_1'
    """
    # Define the replacement function
    def replacer(m: re.Match) -> str:
        # m.group(0) is the matched character
        char = m.group(0)
        
        # Apply the simple case flip logic
        return char.upper() if char.islower() else char.lower()

    # Match any single alphabetic character (a-z or A-Z)
    return re.sub(r'[a-zA-Z]', replacer, string)


funcs = [func1, func2, func3, func4, func5]