# The programming specification:
# def eat(number, need, remaining):
#     """
#     You're a hungry rabbit, and you already have eaten a certain number of carrots,
#     but now you need to eat more carrots to complete the day's meals.
#     you should return an array of [ total number of eaten carrots after your meals,
#     the number of carrots left after your meals ]
#     if there are not enough remaining carrots, you will eat all remaining carrots, but will still be hungry.
#     """

# ----------------------------------------------------------------------
# func1: Direct If/Else Block
# ----------------------------------------------------------------------
def func1(number, need, remaining):
    """Handles the two cases (enough/not enough) with a standard if/else."""
    if remaining >= need:
        # Enough carrots: eat exactly what's needed
        eaten_now = need
    else:
        # Not enough: eat all remaining carrots
        eaten_now = remaining
    
    total_eaten = number + eaten_now
    carrots_left = remaining - eaten_now
    
    return [total_eaten, carrots_left]

# ----------------------------------------------------------------------
# func2: Using min() for Carrots Eaten (Most Idiomatic)
# ----------------------------------------------------------------------
def func2(number, need, remaining):
    """Uses the min() function for a concise calculation of carrots eaten."""
    # The rabbit eats the minimum of what is needed and what is available.
    eaten_now = min(need, remaining)
    
    total_eaten = number + eaten_now
    carrots_left = remaining - eaten_now
    
    return [total_eaten, carrots_left]

# ----------------------------------------------------------------------
# func3: Calculating Remaining First
# ----------------------------------------------------------------------
def func3(number, need, remaining):
    """Calculates the difference between remaining and need to determine the case."""
    # Negative means a shortage, positive/zero means enough
    diff = remaining - need
    
    if diff >= 0:
        # Enough carrots: ate 'need'
        total_eaten = number + need
        carrots_left = diff
    else:
        # Not enough: ate 'remaining'
        total_eaten = number + remaining
        carrots_left = 0
        
    return [total_eaten, carrots_left]

# ----------------------------------------------------------------------
# func4: Concise Conditional Expression (Ternary)
# ----------------------------------------------------------------------
def func4(number, need, remaining):
    """Uses the Python ternary operator for a concise expression."""
    # Set 'eaten_now' using a conditional expression
    eaten_now = need if remaining >= need else remaining
    
    # Calculate 'carrots_left'
    carrots_left = remaining - eaten_now
    
    total_eaten = number + eaten_now
    
    return [total_eaten, carrots_left]

# ----------------------------------------------------------------------
# func5: Calculating Leftover Need
# ----------------------------------------------------------------------
def func5(number, need, remaining):
    """Calculates how much is still needed (negative means surplus)."""
    # Calculate how many carrots the rabbit *still needs*
    leftover_need = need - remaining
    
    if leftover_need <= 0:
        # Need was met. Leftovers are the absolute value of the negative need.
        carrots_left = abs(leftover_need)
        eaten_now = need
    else:
        # Need was NOT met. All 'remaining' were eaten.
        carrots_left = 0
        eaten_now = remaining
        
    total_eaten = number + eaten_now
    
    return [total_eaten, carrots_left]


# Example Usage and Verification:
# if __name__ == '__main__':
#     examples = [
#         (5, 6, 10, [11, 4]),  # Enough stock
#         (4, 8, 9, [12, 1]),   # Enough stock
#         (1, 10, 10, [11, 0]), # Exactly enough stock
#         (2, 11, 5, [7, 0])    # Not enough stock
#     ]

#     functions = [func1, func2, func3, func4, func5]

#     print("--- Function Verification ---")
#     for func in functions:
#         func_name = func.__name__
#         print(f"\nTesting {func_name}:")
#         for number, need, remaining, expected in examples:
#             result = func(number, need, remaining)
#             status = "PASS" if result == expected else f"FAIL (Expected: {expected}, Got: {result})"
#             print(f"  eat({number}, {need}, {remaining}) -> {result} | {status}")

sedit_gemini = [func1, func2, func3, func4, func5]