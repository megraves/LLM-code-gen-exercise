import itertools

# --- Problem: make_a_pile(n) ---
# Arithmetic Progression: a_i = n + 2 * (i - 1) for i = 1 to n.
# Common difference d = 2.

def func1(n):
    """
    func1: Iterative Approach with Arithmetic Formula.
    Uses a standard for loop and the formula a_i = n + 2*(i-1) to calculate each term.
    """
    pile = []
    # i represents the level number, from 1 to n
    for i in range(1, n + 1):
        stones = n + 2 * (i - 1)
        pile.append(stones)
    return pile

def func2(n):
    """
    func2: Iterative Approach with Update Variable.
    Starts at 'n' and iteratively adds 2 to the current stone count in each step.
    """
    pile = []
    current_stones = n
    
    # Loop n times for n levels
    for _ in range(n):
        pile.append(current_stones)
        current_stones += 2
        
    return pile

def func3(n):
    """
    func3: List Comprehension with Arithmetic Formula.
    A concise, "Pythonic" version of func1 using a list comprehension.
    """
    # i is the level index starting from 1 up to n
    return [n + 2 * (i - 1) for i in range(1, n + 1)]

def func4(n):
    """
    func4: Using itertools.count and islice.
    Generates an infinite sequence (n, n+2, n+4, ...) and takes the first n elements.
    Requires 'import itertools'.
    """
    # count(start, step) generates the sequence; islice(iterable, stop) takes n elements
    return list(itertools.islice(itertools.count(n, 2), n))

def func5(n):
    """
    func5: Using the built-in range function.
    Leverages the fact that the sequence is an arithmetic progression with step=2.
    The stop value must be exclusive: stop = a_n + 2 = (3*n - 2) + 2 = 3*n.
    """
    # range(start, stop, step)
    stop_value = 3 * n
    return list(range(n, stop_value, 2))


# --- Debugging/Testing Section ---
# Define test cases
test_cases = [
    (3, [3, 5, 7]),  # Odd n, next odd
    (4, [4, 6, 8, 10]),  # Even n, next even
    (1, [1]),
    (6, [6, 8, 10, 12, 14, 16])
]

functions = [func1, func2, func3, func4, func5]

# Run tests and print results
print("--- Debugging Test Run ---")
for i, func in enumerate(functions):
    func_name = f"func{i+1}"
    print(f"\nTesting {func_name}:")
    
    all_passed = True
    for n, expected in test_cases:
        result = func(n)
        status = "PASSED" if result == expected else "FAILED"
        if status == "FAILED":
            all_passed = False
            print(f"  Input n={n}: Expected {expected}, Got {result} ({status})")
        
    if all_passed:
        print(f"  All {len(test_cases)} tests passed for {func_name}. ✅")


# --- General Debugging Review Summary ---

# 1. func1 (Iterative Formula):
#    - Review: **Robust and explicit**. Directly implements the math formula.
#    - Bug Risk: Low. Only potential bug is off-by-one in the (i-1) calculation if range is wrong. (Correct)
# 
# 2. func2 (Iterative Update):
#    - Review: **Clear and efficient** for large n as it avoids multiplication in the loop.
#    - Bug Risk: Low. The logic of starting at 'n' and adding 2 repeatedly is correct.
#
# 3. func3 (List Comprehension):
#    - Review: **Concise and Pythonic**. Same logic as func1 but in one line.
#    - Bug Risk: Low. Relies on the same correct formula.
# 
# 4. func4 (itertools):
#    - Review: **Functional approach**. Excellent for demonstrating knowledge of `itertools`.
#    - Bug Risk: Moderate. Incorrect use of `islice` arguments (start, stop, step) or forgetting the final `list()` conversion could break it. (Correct usage: `islice(iterable, stop)`)
#
# 5. func5 (range):
#    - Review: **Most optimized for speed**, using a highly optimized C-implemented built-in function.
#    - Bug Risk: High. The crucial part is correctly calculating the **exclusive stop value** ($3n$). A common mistake is using the last term ($3n-2$) as the stop value. (Correct: $3n$)

sdebug_gemini = [func1, func2, func3, func4, func5]