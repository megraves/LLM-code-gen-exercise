import itertools

# The problem defines an arithmetic progression:
# First term: a_1 = n
# Common difference: d = 2
# The i-th term (where i starts at 0 for list index) is: n + 2 * i
# The number of terms is n.

def func1(n):
    """
    Iterative solution using a simple loop and list append.
    Time Complexity: O(n)
    """
    pile = []
    current_stones = n
    for _ in range(n):
        pile.append(current_stones)
        current_stones += 2
    return pile

# ---

def func2(n):
    """
    Solution using a list comprehension and the arithmetic progression formula.
    Time Complexity: O(n)
    """
    # i represents the index, starting from 0.
    return [n + 2 * i for i in range(n)]

# ---

def func3(n):
    """
    Solution using the built-in range() function with a step size of 2, 
    then converting the range object to a list.
    The sequence is [n, n+2, n+4, ..., n + 2*(n-1)].
    The stop value for range() must be n + 2*n = 3*n to be exclusive.
    Time Complexity: O(n)
    """
    # start=n, step=2. stop=3*n (exclusive)
    return list(range(n, 3 * n, 2))

# ---

def func4(n):
    """
    Solution using itertools.count to generate the infinite sequence 
    and itertools.islice to efficiently take exactly n elements.
    Time Complexity: O(n)
    """
    # count(n, 2) starts at n and steps by 2.
    # islice takes the first n elements.
    return list(itertools.islice(itertools.count(n, 2), n))

# ---

def func5(n):
    """
    Recursive solution that calculates the last element of the n-level pile 
    and appends it to the result of the (n-1) level pile.
    Time Complexity: O(n) due to n recursive calls and list concatenations.
    """
    if n == 1:
        return [1]
    
    # The value of the nth (last) element is a_n = n + 2*(n-1) = 3n - 2
    last_stone_count = 3 * n - 2
    
    # The pile of n levels is the pile of n-1 levels plus the last element.
    # Note: List concatenation (pile + [element]) creates a new list at each step, 
    # making this approach generally less performant than iterative methods in Python.
    return func5(n - 1) + [last_stone_count]

# Example Usage:
# print(f"func1(3): {func1(3)}")
# print(f"func2(3): {func2(3)}")
# print(f"func3(5): {func3(5)}")
# print(f"func4(5): {func4(5)}")
# print(f"func5(5): {func5(5)}")

cot_gemini = [func1, func2, func3, func4, func5]