import re

def func1(s):
    """
    Replace commas with spaces, split on spaces, filter out empty strings.
    """
    s = s.replace(",", " ")
    return [word for word in s.split() if word]

def func2(s):
    """
    Use regex to split on one or more spaces or commas.
    """
    return re.split(r'[,\s]+', s.strip())

def func3(s):
    """
    Manual iteration: build words character by character, split on space or comma.
    """
    words = []
    temp = ""
    for char in s:
        if char in " ,":
            if temp:
                words.append(temp)
                temp = ""
        else:
            temp += char
    if temp:
        words.append(temp)
    return words

def func4(s):
    """
    Split by commas first, then split each part by spaces, flatten the result.
    """
    result = []
    for part in s.split(","):
        result.extend(part.strip().split())
    return result

def func5(s):
    """
    Replace commas with spaces, split on spaces, use filter to remove empty strings.
    """
    return list(filter(None, s.replace(",", " ").split()))


splan_gpt = [func1, func2, func3, func4, func5]