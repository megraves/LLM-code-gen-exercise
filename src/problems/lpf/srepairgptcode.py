import math
import random

# ------------------------------------------------------------
# func1 — Basic trial division
# ------------------------------------------------------------
def func1(n: int) -> int:
    """Basic trial division method."""
    factor = 2
    last_factor = 1
    while n > 1:
        if n % factor == 0:
            last_factor = factor
            while n % factor == 0:
                n //= factor
        factor += 1
    return last_factor


# ------------------------------------------------------------
# func2 — Optimized trial division (checks up to sqrt(n))
# ------------------------------------------------------------
def func2(n: int) -> int:
    """Optimized trial division method."""
    largest = 1
    while n % 2 == 0:
        largest = 2
        n //= 2
    factor = 3
    while factor * factor <= n:
        if n % factor == 0:
            largest = factor
            while n % factor == 0:
                n //= factor
        factor += 2
    if n > 2:
        largest = n
    return largest


# ------------------------------------------------------------
# func3 — Recursive approach
# ------------------------------------------------------------
def func3(n: int, f: int = 2) -> int:
    """Recursive version of prime factor search."""
    if n == f:
        return f
    if n % f == 0:
        return func3(n // f, f)
    return func3(n, f + 1)


# ------------------------------------------------------------
# func4 — Prime generator-based approach
# ------------------------------------------------------------
def primes():
    """Generator for prime numbers."""
    yield 2
    n = 3
    while True:
        for p in range(3, int(n ** 0.5) + 1, 2):
            if n % p == 0:
                break
        else:
            yield n
        n += 2


def func4(n: int) -> int:
    """Uses a prime generator to find the largest prime factor."""
    largest = 1
    for p in primes():
        if p * p > n:
            break
        while n % p == 0:
            largest = p
            n //= p
    if n > 1:
        largest = n
    return largest


# ------------------------------------------------------------
# func5 — Pollard’s Rho algorithm (for large numbers)
# ------------------------------------------------------------
def func5(n: int) -> int:
    """Pollard’s Rho algorithm to find the largest prime factor."""

    def gcd(a, b):
        while b:
            a, b = b, a % b
        return a

    def pollards_rho(n):
        if n % 2 == 0:
            return 2
        x = random.randrange(2, n - 1)
        y = x
        c = random.randrange(1, n - 1)
        d = 1
        while d == 1:
            x = (x * x + c) % n
            y = (y * y + c) % n
            y = (y * y + c) % n
            d = gcd(abs(x - y), n)
        return d

    def largest_factor(n):
        if n == 1:
            return 1
        if all(n % i for i in range(2, int(math.sqrt(n)) + 1)):
            return n
        factor = pollards_rho(n)
        return max(largest_factor(factor), largest_factor(n // factor))

    return largest_factor(n)


srepair_gpt = [func1, func2, func3, func4, func5]