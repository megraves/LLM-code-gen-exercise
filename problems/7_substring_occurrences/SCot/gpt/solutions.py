import re

# Solution 1: Sliding window
def func1(string: str, substring: str) -> int:
    count = 0
    for i in range(len(string) - len(substring) + 1):
        if string[i:i+len(substring)] == substring:
            count += 1
    return count

# Solution 2: Using str.find with step 1
def func2(string: str, substring: str) -> int:
    count = 0
    start = 0
    while True:
        pos = string.find(substring, start)
        if pos == -1:
            break
        count += 1
        start = pos + 1  # allow overlap
    return count

# Solution 3: Regular expressions
def func3(string: str, substring: str) -> int:
    if not substring:
        return 0
    return len(list(re.finditer(f'(?={re.escape(substring)})', string)))

# Solution 4: Recursion
def func4(string: str, substring: str) -> int:
    if len(string) < len(substring):
        return 0
    if string[:len(substring)] == substring:
        return 1 + func4(string[1:], substring)
    else:
        return func4(string[1:], substring)

# Solution 5: Sliding slices with sum
def func5(string: str, substring: str) -> int:
    return sum(1 for i in range(len(string) - len(substring) + 1) 
               if string[i:i+len(substring)] == substring)


funcs = [func1, func2, func3, func4, func5]