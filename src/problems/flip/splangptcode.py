# flip_case_solutions.py

"""
Five different implementations of flip_case:
For a given string, flip lowercase letters to uppercase and uppercase letters to lowercase.
Non-alphabetic characters remain unchanged.
"""

# -------------------------
# Solution 1: Using swapcase()
# -------------------------
def func1(string: str) -> str:
    return string.swapcase()


# -------------------------
# Solution 2: Using for loop
# -------------------------
def func2(string: str) -> str:
    result = ""
    for char in string:
        if char.islower():
            result += char.upper()
        elif char.isupper():
            result += char.lower()
        else:
            result += char
    return result


# -------------------------
# Solution 3: Using list comprehension
# -------------------------
def func3(string: str) -> str:
    return ''.join([c.upper() if c.islower() else c.lower() if c.isupper() else c for c in string])


# -------------------------
# Solution 4: Using map() with helper function
# -------------------------
def func4(string: str) -> str:
    def flip(c):
        if c.islower():
            return c.upper()
        elif c.isupper():
            return c.lower()
        else:
            return c
    return ''.join(map(flip, string))


# -------------------------
# Solution 5: Using str.translate() and str.maketrans()
# -------------------------
def func5(string: str) -> str:
    import string as str_module
    trans_table = str_module.ascii_lowercase.upper() + str_module.ascii_uppercase.lower()
    table = str_module.maketrans(str_module.ascii_lowercase + str_module.ascii_uppercase, trans_table)
    return string.translate(table)


# -------------------------
# Example usage
# -------------------------
if __name__ == "__main__":
    test_strings = ["Hello", "Python3!", "123ABCabc"]
    funcs = [func1, func2, func3, func4, func5]

    for f in funcs:
        print(f"{f.__name__} results:")
        for s in test_strings:
            print(f"  {s} -> {f(s)}")
        print()

splan_gpt = [func1, func2, func3, func4, func5]