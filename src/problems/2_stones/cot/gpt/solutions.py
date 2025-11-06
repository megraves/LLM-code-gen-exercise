# Solution 1: Simple iterative approach
def func1(n):
    pile = []
    current = n
    for _ in range(n):
        pile.append(current)
        current += 2  # always next odd/even preserves parity
    return pile

# Solution 2: Using list comprehension
def func2(n):
    return [n + 2*i for i in range(n)]

# Solution 3: Recursive approach
def func3(n, level=0, pile=None):
    if pile is None:
        pile = []
    if level == n:
        return pile
    if level == 0:
        current = n
    else:
        current = pile[-1] + 2
    pile.append(current)
    return func3(n, level+1, pile)

# Solution 4: Using arithmetic sequence formula
def func4(n):
    # Each level increments by 2 from the first
    return [n + 2*i for i in range(n)]

# Solution 5: Using itertools.accumulate
from itertools import accumulate, repeat
def func5(n):
    start = n
    return list(accumulate(repeat(2, n), initial=start))[:-1]


funcs = [func1, func2, func3, func4, func5]