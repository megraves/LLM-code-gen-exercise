
def func1(lst):
    """
    func1: Standard for loop iterating by index.
    
    Given a non-empty list of integers, return the sum of all of the 
    odd elements that are in even positions (indices 0, 2, 4, ...).
    """
    total = 0
    # Iterate through indices 0, 1, 2, 3, ...
    for i in range(len(lst)):
        # Check for even position (index i)
        if i % 2 == 0:
            element = lst[i]
            # Check for odd element
            if element % 2 != 0:
                total += element
    return total

# ---

def func2(lst):
    """
    func2: For loop using a step of 2 to only iterate over even indices.
    """
    total = 0
    # Iterate over even indices: 0, 2, 4, ...
    for i in range(0, len(lst), 2):
        element = lst[i]
        # Check for odd element
        if element % 2 != 0:
            total += element
    return total

# ---

def func3(lst):
    """
    func3: Using enumerate to get both index and element.
    """
    total = 0
    # i is the index, element is the value
    for i, element in enumerate(lst):
        # Check for even position (index i)
        if i % 2 == 0:
            # Check for odd element
            if element % 2 != 0:
                total += element
    return total

# ---

def func4(lst):
    """
    func4: Using a concise generator expression with sum().
    This is often considered the most Pythonic approach.
    """
    return sum(element for i, element in enumerate(lst) 
               if i % 2 == 0 and element % 2 != 0)

# ---

def func5(lst):
    """
    func5: Using list slicing to select elements at even positions, 
    then summing the odd ones from the resulting slice.
    """
    # lst[::2] creates a new list containing elements at indices 0, 2, 4, ...
    elements_at_even_pos = lst[::2]
    total = 0
    
    # Iterate only through the elements that were at even positions
    for element in elements_at_even_pos:
        # Check for odd element
        if element % 2 != 0:
            total += element
    return total

funcs = [func1, func2, func3, func4, func5]