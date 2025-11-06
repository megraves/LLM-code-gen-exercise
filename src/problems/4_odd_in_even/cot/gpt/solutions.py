# sum of odd elements at even positions

def func1(lst):
    total = 0
    for i in range(len(lst)):
        if i % 2 == 0 and lst[i] % 2 != 0:
            total += lst[i]
    return total

def func2(lst):
    total = 0
    for idx, val in enumerate(lst):
        if idx % 2 == 0 and val % 2 != 0:
            total += val
    return total

def func3(lst):
    return sum([val for idx, val in enumerate(lst) if idx % 2 == 0 and val % 2 != 0])

def func4(lst):
    return sum(x for x in lst[::2] if x % 2 != 0)

def func5(lst):
    return sum(filter(lambda x: x % 2 != 0, lst[::2]))

funcs = [func1, func2, func3, func4, func5]