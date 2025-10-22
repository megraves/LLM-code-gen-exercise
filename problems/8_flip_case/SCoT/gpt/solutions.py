from typing import Callable
import string
import re

def func1(s: str) -> str:
    """
    Implementation 1 — use built-in str.swapcase (simple, concise).
    Behavior: uses Python's Unicode-aware swapcase.
    """
    return s.swapcase()

def func2(s: str) -> str:
    """
    Implementation 2 — list comprehension with islower()/isupper() checks.
    Behavior: Unicode-aware (follows Python's .upper()/.lower()).
    """
    return ''.join(
        (ch.upper() if ch.islower() else (ch.lower() if ch.isupper() else ch))
        for ch in s
    )

def func3(s: str) -> str:
    """
    Implementation 3 — str.translate using an ASCII-only translation table.
    Behavior: FAST for ASCII; non-ASCII letters are left unchanged.
    Note: This only maps A-Z <-> a-z for ASCII characters.
    """
    lower = string.ascii_lowercase  # 'abcdefghijklmnopqrstuvwxyz'
    upper = string.ascii_uppercase  # 'ABCDEFGHIJKLMNOPQRSTUVWXYZ'
    trans = str.maketrans(lower + upper, upper + lower)
    return s.translate(trans)

def func4(s: str) -> str:
    """
    Implementation 4 — manual ord/chr arithmetic for ASCII letters.
    Behavior: ASCII-only; non-ASCII characters are left as-is.
    (This avoids calling .upper()/.lower() per character.)
    """
    out_chars = []
    for ch in s:
        o = ord(ch)
        # 'a'..'z' -> 'A'..'Z'
        if 97 <= o <= 122:
            out_chars.append(chr(o - 32))
        # 'A'..'Z' -> 'a'..'z'
        elif 65 <= o <= 90:
            out_chars.append(chr(o + 32))
        else:
            out_chars.append(ch)
    return ''.join(out_chars)

def func5(s: str) -> str:
    """
    Implementation 5 — regex substitution with a lambda that flips case.
    Behavior: Unicode-aware because it uses .isupper()/.islower()/.lower()/.upper().
    """
    def flip(match: re.Match) -> str:
        ch = match.group(0)
        return ch.lower() if ch.isupper() else ch.upper()
    # Only target letter characters in the A-Za-z range for the regex,
    # but we rely on .isupper()/.islower() to decide exact behavior.
    # Using [A-Za-z] keeps the regex fast; change to r'\w' or r'\p{L}' with regex module for more coverage.
    return re.sub(r'[A-Za-z]', flip, s)

funcs = [func1, func2, func3, func4, func5]