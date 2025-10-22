# eat_carrots.py

# Solution 1: Simple if/else
def func1(number, need, remaining):
    if remaining >= need:
        return [number + need, remaining - need]
    else:
        return [number + remaining, 0]

# Solution 2: Using min()
def func2(number, need, remaining):
    eaten = min(need, remaining)
    return [number + eaten, remaining - eaten]

# Solution 3: Using max() to avoid negative remaining
def func3(number, need, remaining):
    eaten = min(need, remaining)
    remaining_after = max(remaining - need, 0)
    return [number + eaten, remaining_after]

# Solution 4: Using conditional expression (ternary)
def func4(number, need, remaining):
    return [number + need, remaining - need] if remaining >= need else [number + remaining, 0]

# Solution 5: Using min() and tuple unpacking
def func5(number, need, remaining):
    eaten = min(need, remaining)
    total, remaining_after = number + eaten, remaining - eaten
    return [total, remaining_after]

# Test examples
if __name__ == "__main__":
    test_cases = [
        (5, 6, 10),
        (4, 8, 9),
        (1, 10, 10),
        (2, 11, 5),
        (3, 2, 1)
    ]

    for i, (number, need, remaining) in enumerate(test_cases, 1):
        print(f"Test case {i}:")
        print("func1:", func1(number, need, remaining))
        print("func2:", func2(number, need, remaining))
        print("func3:", func3(number, need, remaining))
        print("func4:", func4(number, need, remaining))
        print("func5:", func5(number, need, remaining))
        print()


funcs = [func1, func2, func3, func4, func5]