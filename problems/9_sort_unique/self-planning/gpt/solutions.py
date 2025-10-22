from typing import List
import itertools


def func1(l: List[int]) -> List[int]:
    """Use set() and sorted()
    >>> func1([5, 3, 5, 2, 3, 3, 9, 0, 123])
    [0, 2, 3, 5, 9, 123]
    """
    unique_elements = set(l)
    result = sorted(unique_elements)
    return result


def func2(l: List[int]) -> List[int]:
    """Manual duplicate filtering
    >>> func2([5, 3, 5, 2, 3, 3, 9, 0, 123])
    [0, 2, 3, 5, 9, 123]
    """
    unique_list = []
    for item in l:
        if item not in unique_list:
            unique_list.append(item)
    return sorted(unique_list)


def func3(l: List[int]) -> List[int]:
    """Use dict.fromkeys()
    >>> func3([5, 3, 5, 2, 3, 3, 9, 0, 123])
    [0, 2, 3, 5, 9, 123]
    """
    unique_dict = dict.fromkeys(l)
    return sorted(unique_dict.keys())


def func4(l: List[int]) -> List[int]:
    """Use set tracking inside comprehension
    >>> func4([5, 3, 5, 2, 3, 3, 9, 0, 123])
    [0, 2, 3, 5, 9, 123]
    """
    seen = set()
    unique_ordered = [x for x in l if not (x in seen or seen.add(x))]
    return sorted(unique_ordered)


def func5(l: List[int]) -> List[int]:
    """Use itertools.groupby() after sorting
    >>> func5([5, 3, 5, 2, 3, 3, 9, 0, 123])
    [0, 2, 3, 5, 9, 123]
    """
    sorted_list = sorted(l)
    unique_sorted = [key for key, _ in itertools.groupby(sorted_list)]
    return unique_sorted


if __name__ == "__main__":
    test_input = [5, 3, 5, 2, 3, 3, 9, 0, 123]
    expected_output = [0, 2, 3, 5, 9, 123]

    for f in [func1, func2, func3, func4, func5]:
        result = f(test_input)
        print(f"{f.__name__}: {result} (✓ {result == expected_output})")


funcs = [func1, func2, func3, func4, func5]