def how_many_times(string: str, substring: str) -> int:
    """ Find how many times a given substring can be found in the original string. Count overlaping cases.
    >>> how_many_times('', 'a')
    0
    >>> how_many_times('aaa', 'a')
    3
    >>> how_many_times('aaaa', 'aa')
    3
    """
    # Handle edge case where substring is empty to prevent errors.
    if not substring:
        return 0

    count = 0
    # Iterate through the string. The loop stops where the remaining
    # part of the string is no longer long enough to contain the substring.
    for i in range(len(string) - len(substring) + 1):
        # Check if the slice of the string starting at the current index
        # and with the length of the substring is equal to the substring.
        if string[i:i + len(substring)] == substring:
            count += 1
    
    return count