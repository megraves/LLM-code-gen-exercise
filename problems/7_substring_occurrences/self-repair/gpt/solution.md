Here’s a Python program implementing **five different valid solutions** to the same specification — each using a distinct method or algorithmic idea.

All versions pass the given doctests and correctly handle overlapping substrings.

---

```python
def func1(string: str, substring: str) -> int:
    """Simple loop using str.startswith to detect overlapping substrings."""
    if not string or not substring:
        return 0
    count = 0
    for i in range(len(string) - len(substring) + 1):
        if string.startswith(substring, i):
            count += 1
    return count


def func2(string: str, substring: str) -> int:
    """Sliding window comparison."""
    if not string or not substring:
        return 0
    count = 0
    sub_len = len(substring)
    for i in range(len(string) - sub_len + 1):
        if string[i:i + sub_len] == substring:
            count += 1
    return count


def func3(string: str, substring: str) -> int:
    """Use regular expressions with lookahead to count overlapping matches."""
    import re
    if not string or not substring:
        return 0
    pattern = f"(?={re.escape(substring)})"
    return len(re.findall(pattern, string))


def func4(string: str, substring: str) -> int:
    """Recursive implementation counting overlaps."""
    if not string or not substring:
        return 0
    idx = string.find(substring)
    if idx == -1:
        return 0
    return 1 + func4(string[idx + 1:], substring)


def func5(string: str, substring: str) -> int:
    """While loop using str.find with manual index management for overlap."""
    if not string or not substring:
        return 0
    count = 0
    start = 0
    while True:
        pos = string.find(substring, start)
        if pos == -1:
            break
        count += 1
        start = pos + 1  # move one step to allow overlapping
    return count
```

---

### ✅ Test Results

All these functions satisfy:

```python
print(func1('', 'a'))        # 0
print(func1('aaa', 'a'))     # 3
print(func1('aaaa', 'aa'))   # 3
```

and equivalently for `func2` through `func5`.

---

Would you like me to also benchmark or compare these (e.g., efficiency on long strings)?
