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

# Optional: a small runner to demonstrate behavior for examples / tests
if __name__ == "__main__":
    examples = [
        "Hello",
        "",
        "123 AbC!",
        "ß",                # special unicode (sharp s)
        "Σσ",               # Greek sigma examples
        "mañana",           # contains non-ASCII letter ñ
        "Mixed: aB1!@#Zz"
    ]

    funcs: list[tuple[str, Callable[[str], str]]] = [
        ("func1 (swapcase)", func1),
        ("func2 (comp)", func2),
        ("func3 (translate ASCII)", func3),
        ("func4 (ord/chr ASCII)", func4),
        ("func5 (regex)", func5),
    ]

    for text in examples:
        print(f"Input: {repr(text)}")
        for name, f in funcs:
            print(f"  {name}: {repr(f(text))}")
        print()


funcs = [func1, func2, func3, func4, func5]