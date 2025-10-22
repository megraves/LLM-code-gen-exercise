def func1(number, need, remaining):
    if remaining >= need:
        return [number + need, remaining - need]
    else:
        return [number + remaining, 0]


def func2(number, need, remaining):
    eaten = min(need, remaining)
    return [number + eaten, remaining - eaten]


def func3(number, need, remaining):
    total_eaten = number + min(need, remaining)
    remaining_after = max(remaining - need, 0)
    return [total_eaten, remaining_after]


def func4(number, need, remaining):
    return [number + (need if remaining >= need else remaining),
            remaining - need if remaining >= need else 0]


def func5(number, need, remaining):
    import operator
    eaten = min(need, remaining)
    return list(map(lambda f: f(number, eaten, remaining), [lambda n,e,r: n+e, lambda n,e,r: r-e]))


# Example usage / testing
if __name__ == "__main__":
    examples = [
        (5, 6, 10),
        (4, 8, 9),
        (1, 10, 10),
        (2, 11, 5)
    ]
    
    for f in [func1, func2, func3, func4, func5]:
        print(f"{f.__name__}:")
        for ex in examples:
            print(f"  {ex} -> {f(*ex)}")
        print()


funcs = [func1, func2, func3, func4, func5]