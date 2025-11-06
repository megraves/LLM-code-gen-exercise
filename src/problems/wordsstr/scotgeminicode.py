import re
from itertools import chain

def func1(s):
    """
    Solution 1: Sequential Replace and Split (Simple String Manipulation)
    1. Replaces all commas with a single space.
    2. Uses the default str.split(), which handles multiple spaces 
       and automatically filters out resulting empty strings.
    """
    # Step 1: Normalize all delimiters to a single space
    temp_s = s.replace(',', ' ')
    
    # Step 2: Split by space. The default split() handles multiple spaces 
    # and leading/trailing spaces gracefully.
    result = temp_s.split()
    
    return result

# ----------------------------------------------------------------------

def func2(s):
    """
    Solution 2: Using re.split() (Regular Expressions)
    1. Uses the re.split() function to split the string.
    2. The regex pattern '[, ]+' matches one or more occurrences of either 
       a comma OR a space, acting as the delimiter.
    3. Filters out any empty strings that might result from leading/trailing delimiters.
    """
    # Pattern: Match one or more commas (,) OR spaces ( )
    delimiters = r'[, ]+'
    
    # Split the string
    temp_list = re.split(delimiters, s)
    
    # Filter out empty strings that result from leading/trailing delimiters
    result = [word for word in temp_list if word]
    
    return result

# ----------------------------------------------------------------------

def func3(s):
    """
    Solution 3: Using itertools.chain.from_iterable and Splitting
    1. Splits the string by the primary delimiter (comma).
    2. Iterates over the resulting list, splitting each item by the 
       secondary delimiter (space).
    3. Uses chain.from_iterable to flatten the list of lists into a single list.
    """
    # Step 1 & 2: Split by comma, then split each resulting piece by space
    intermediate_list = [piece.split() for piece in s.split(',')]
    
    # Step 3: Flatten the list of lists. split() implicitly handles filtering empty strings 
    # that result from multiple spaces or leading/trailing spaces in the pieces.
    result = list(chain.from_iterable(intermediate_list))
    
    # Final filter for robustness (e.g., if the original string was just ",")
    return [word for word in result if word]

# ----------------------------------------------------------------------

def func4(s):
    """
    Solution 4: Two-Pass Cleaning and Splitting
    1. Replaces commas with spaces.
    2. Iteratively cleans up multiple spaces to single spaces (robust normalization).
    3. Strips leading/trailing spaces.
    4. Splits the clean string by the single space.
    """
    # Step 1: Replace all commas with a single space
    temp_s = s.replace(',', ' ')
    
    # Step 2: Ensure only single spaces exist between words
    # This loop cleans up "word  word", "word   word", etc.
    while '  ' in temp_s:
        temp_s = temp_s.replace('  ', ' ')
        
    # Step 3: Strip any resulting leading/trailing spaces
    clean_s = temp_s.strip()
    
    # Step 4: Split by the single space
    if not clean_s:
        return []
        
    result = clean_s.split(' ')
    
    return result

# ----------------------------------------------------------------------

def func5(s):
    """
    Solution 5: Splitting by Space and Then Filtering/Splitting Commas
    1. Splits the string by space first (using default split() for robustness).
    2. Iterates over the resulting "word groups".
    3. If a group contains a comma, it is further split by the comma; otherwise, it's appended directly.
    """
    # Step 1: Split by space (robust against multiple spaces)
    space_split_list = s.split()
    
    final_words = []
    
    # Step 2 & 3: Iterate and handle internal commas
    for word_group in space_split_list:
        if ',' in word_group:
            # Split the group by comma and extend the final list, filtering out empty strings
            comma_split_words = [word for word in word_group.split(',') if word]
            final_words.extend(comma_split_words)
        else:
            # If no comma, it's a clean word
            final_words.append(word_group)
            
    return final_words

# ----------------------------------------------------------------------
# Example Usage:
# ----------------------------------------------------------------------

test_string = "apple,banana orange,grape,  kiwi "
print(f"Input: '{test_string}'")

print(f"func1 (Replace/Default Split): {func1(test_string)}")
print(f"func2 (re.split):              {func2(test_string)}")
print(f"func3 (itertools/Nested Split): {func3(test_string)}")
print(f"func4 (Two-Pass Clean/Split):  {func4(test_string)}")
print(f"func5 (Iterative Split):       {func5(test_string)}")

# Expected Output for all: ['apple', 'banana', 'orange', 'grape', 'kiwi']

scot_gemini = [func1, func2, func3, func4, func5]