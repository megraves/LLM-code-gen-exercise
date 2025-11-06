import re

def func1(s):
    """Remove commas and split by spaces."""
    s_clean = s.replace(",", "")
    return s_clean.split()

def func2(s):
    """Use regex to split by commas or whitespace."""
    return re.split(r'[,\s]+', s.strip())

def func3(s):
    """Replace commas with spaces and build list with comprehension-like loop."""
    words = []
    for word in s.replace(",", " ").split():
        if word:
            words.append(word)
    return words

def func4(s):
    """Use filter to remove empty strings after replacing commas with spaces."""
    return list(filter(None, s.replace(",", " ").split()))

def func5(s):
    """Use regex to find all word sequences."""
    return re.findall(r'\b\w+\b', s)

scot_gpt = [func1, func2, func3, func4, func5]