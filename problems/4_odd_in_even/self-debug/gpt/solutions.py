# sum of odd elements in even positions

def func1(lst):
    total = 0
    for i in range(0, len(lst), 2):  # even positions
        if lst[i] % 2 == 1:           # odd number
            total += lst[i]
    return total

def func2(lst):
    total = 0
    for idx, val in enumerate(lst):
        if idx % 2 == 0 and val % 2 == 1:
            total += val
    return total

def func3(lst):
    return sum(val for idx, val in enumerate(lst) if idx % 2 == 0 and val % 2 == 1)

def func4(lst):
    return sum(lst[i] for i in range(0, len(lst), 2) if lst[i] % 2 == 1)

def func5(lst):
    even_positions = lst[::2]                  # elements at even positions
    odd_elements = filter(lambda x: x % 2 == 1, even_positions)
    return sum(odd_elements)



funcs = [func1, func2, func3, func4, func5]