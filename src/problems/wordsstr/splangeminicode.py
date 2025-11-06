import re
from itertools import groupby

def func1(s: str) -> list[str]:
    """
    Solution 1: The most Pythonic approach.
    Replaces all commas with spaces, then uses the default str.split()
    behavior, which splits on any sequence of whitespace and automatically
    discards empty strings.

    Robust against multiple delimiters (e.g., "Hi,, there").
    """
    # Step 1: Replace all commas with spaces.
    s_modified = s.replace(',', ' ')

    # Step 2: Use split() without arguments. This splits by any sequence of 
    # whitespace (spaces, tabs, newlines, etc.) and ignores empty results.
    return s_modified.split()

def func2(s: str) -> list[str]:
    """
    Solution 2: Using Regular Expressions.
    Splits the string using re.split based on a pattern matching one or more
    commas OR one or more whitespace characters.
    """
    # Pattern: r'[,\s]+' matches one or more occurrences of either a comma (,) or 
    # any whitespace character (\s, which includes space, tab, newline).
    words = re.split(r'[,\s]+', s)
    
    # Filter out any empty strings that might result from leading/trailing delimiters
    # or edge cases where the pattern doesn't perfectly prevent all empties.
    return [word for word in words if word]

def func3(s: str) -> list[str]:
    """
    Solution 3: Explicit Split and List Comprehension Filter.
    This is less robust than func1 because it relies on the fact that 
    str.split(' ') generates empty strings for multiple spaces, which then
    need to be explicitly filtered out.
    """
    # Step 1: Replace all commas with spaces.
    s_modified = s.replace(',', ' ')

    # Step 2: Split explicitly on a single space ' '. This creates empty strings
    # for double spaces (e.g., 'a  b' -> ['a', '', 'b']).
    words = s_modified.split(' ')
    
    # Step 3: Use a list comprehension to filter out empty strings (i.e., '' or ' ').
    return [word for word in words if word]

def func4(s: str) -> list[str]:
    """
    Solution 4: Procedural Approach (Manual State Machine).
    Iterates through the string character by character, manually building words.
    This avoids relying on built-in split functions, demonstrating a low-level
    implementation.
    """
    words = []
    current_word = ""
    delimiters = {',', ' '}
    
    for char in s:
        if char in delimiters:
            # Separator encountered: If we were building a word, finalize it.
            if current_word:
                words.append(current_word)
                current_word = ""
        else:
            # Word character encountered: Append it to the current word.
            current_word += char
            
    # After the loop, check if the last word was being built and needs appending.
    if current_word:
        words.append(current_word)
        
    return words

def func5(s: str) -> list[str]:
    """
    Solution 5: Functional Grouping with itertools.groupby.
    Groups consecutive characters based on whether they are a delimiter or a word
    character, and then extracts the word groups.
    """
    delimiters = {',', ' '}
    
    # Helper function to determine if a character is a delimiter
    def is_delimiter(char):
        return char in delimiters

    # Group characters. 'key' will be True for delimiters, False for word characters.
    grouped_chars = groupby(s, key=is_delimiter)

    result = []
    for is_sep, group in grouped_chars:
        if not is_sep:
            # If 'is_sep' is False, this group is a word. Join characters and add.
            word = "".join(group)
            if word: # Should always be true, but added for safety
                result.append(word)

    return result


splan_gemini = [func1, func2, func3, func4, func5]