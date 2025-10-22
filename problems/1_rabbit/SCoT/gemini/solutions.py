def eat(number, need, remaining):
    """
    You're a hungry rabbit, and you already have eaten a certain number of carrots,
    but now you need to eat more carrots to complete the day's meals.
    you should return an array of [ total number of eaten carrots after your meals,
    the number of carrots left after your meals ]
    if there are not enough remaining carrots, you will eat all remaining carrots, but will still be hungry.

    Example:
    * eat(5, 6, 10) -> [11, 4]
    * eat(4, 8, 9) -> [12, 1]
    * eat(1, 10, 10) -> [11, 0]
    * eat(2, 11, 5) -> [7, 0]

    Variables:
    @number : integer
    the number of carrots that you have eaten.
    @need : integer
    the number of carrots that you need to eat.
    @remaining : integer
    the number of remaining carrots thet exist in stock

    Constrain:
    * 0 <= number <= 1000
    * 0 <= need <= 1000
    * 0 <= remaining <= 1000
    """
    # This placeholder function is not one of the requested solutions (func1-func5).
    # You would typically call one of the implementations below.
    return func5(number, need, remaining)


def func1(number, need, remaining):
    """
    Solution 1: Uses a basic if/else statement to check if the remaining stock
    is sufficient to meet the need.
    """
    if remaining >= need:
        # Sufficient stock: rabbit eats all it needs
        eaten_total = number + need
        left = remaining - need
    else:
        # Insufficient stock: rabbit eats all remaining
        eaten_total = number + remaining
        left = 0
        
    return [eaten_total, left]


def func2(number, need, remaining):
    """
    Solution 2: Determines the actual amount eaten using min(), then calculates 
    total eaten and remaining stock based on that amount.
    """
    # The rabbit eats the smaller of what it needs and what is available
    eaten_now = min(need, remaining)
    
    # Calculate the outputs based on the amount eaten_now
    eaten_total = number + eaten_now
    left = remaining - eaten_now
    
    return [eaten_total, left]


def func3(number, need, remaining):
    """
    Solution 3: Uses Python's conditional expression (ternary operator) to 
    return the correct list based on the sufficiency of the remaining stock.
    """
    return (
        [number + need, remaining - need]    # Case: sufficient stock (remaining >= need)
        if remaining >= need 
        else [number + remaining, 0]        # Case: insufficient stock
    )


def func4(number, need, remaining):
    """
    Solution 4: Calculates the 'shortfall' (how many fewer carrots were eaten than needed)
    to determine the number of carrots left and eaten now.
    """
    
    # Calculate how many carrots the rabbit needed but *couldn't* eat.
    # If remaining >= need, this shortfall is 0.
    shortfall = max(0, need - remaining)
    
    # Carrots eaten now is need - shortfall
    eaten_now = need - shortfall
    
    eaten_total = number + eaten_now
    
    # Total carrots left: remaining stock minus the amount actually eaten
    left = remaining - eaten_now
    
    return [eaten_total, left]


def func5(number, need, remaining):
    """
    Solution 5: The most concise solution, using the min() function to directly
    determine the amount eaten and calculate the two results simultaneously.
    (Identical logic to func2, but more compact)
    """
    # Amount eaten now is the minimum of what is needed and what is available
    eaten_now = min(need, remaining)
    
    return [
        number + eaten_now,    # Total carrots eaten
        remaining - eaten_now  # Total carrots left
    ]


# --- Examples/Test Cases ---
# print(f"eat(5, 6, 10) -> Expected: [11, 4]")
# print(f"func1: {func1(5, 6, 10)}")
# print(f"func5: {func5(5, 6, 10)}\n")

# print(f"eat(2, 11, 5) -> Expected: [7, 0]")
# print(f"func1: {func1(2, 11, 5)}")
# print(f"func5: {func5(2, 11, 5)}")

funcs = [func1, func2, func3, func4, func5]