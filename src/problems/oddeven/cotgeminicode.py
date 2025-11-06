def func1(lst):
    """
    func1: Traditional 'for' loop (Iterating over even indices)
    Iterates through even indices only and checks for odd elements.
    """
    total = 0
    # Iterate over even indices: 0, 2, 4, ...
    for i in range(0, len(lst), 2):
        element = lst[i]
        # Check if the element at the even index is odd
        if element % 2 != 0:
            total += element
    return total

#----------------------------------------------------------------------

def func2(lst):
    """
    func2: 'for' loop with 'enumerate' (Checking both conditions)
    Uses enumerate to check both index parity and element parity.
    """
    total = 0
    # i is the index, x is the element
    for i, x in enumerate(lst):
        # Check if the index is even (i % 2 == 0)
        # AND if the element is odd (x % 2 != 0)
        if i % 2 == 0 and x % 2 != 0:
            total += x
    return total

#----------------------------------------------------------------------

def func3(lst):
    """
    func3: List Comprehension
    Uses list comprehension with enumerate for a concise solution.
    """
    # Filter for elements where the index 'i' is even AND the element 'x' is odd,
    # and then sum the resulting list of filtered elements.
    return sum([x for i, x in enumerate(lst) if i % 2 == 0 and x % 2 != 0])

#----------------------------------------------------------------------

def func4(lst):
    """
    func4: Slicing and Iterating
    Slices the list to get elements at even positions, then sums the odd ones.
    """
    # Get all elements at even positions: lst[0], lst[2], lst[4], ...
    even_pos_elements = lst[::2]
    
    total = 0
    # Iterate over this subset and check if the element is odd
    for element in even_pos_elements:
        if element % 2 != 0:
            total += element
            
    return total

#----------------------------------------------------------------------

def func5(lst):
    """
    func5: Functional Approach ('filter' and 'lambda')
    Uses filter and a lambda function for a functional approach.
    """
    # Enumerate the list to get (index, element) pairs
    indexed_elements = enumerate(lst)
    
    # Filter the pairs: (i, x) such that i is even AND x is odd
    # item[0] is the index (i), item[1] is the element (x)
    filtered_pairs = filter(lambda item: item[0] % 2 == 0 and item[1] % 2 != 0, indexed_elements)
    
    # Sum the *elements* (item[1]) from the remaining filtered pairs
    return sum(item[1] for item in filtered_pairs)

#----------------------------------------------------------------------

cot_gemini = [func1, func2, func3, func4, func5]