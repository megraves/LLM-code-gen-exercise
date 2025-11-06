# largest_prime_factors.py
import math
import random
from typing import List

def func1(n: int) -> int:
    """Simple trial division.
    Repeatedly divide by the smallest factor found, track the maximum.
    """
    if n < 2:
        raise ValueError("n must be >= 2")
    max_pf = 1
    i = 2
    while i * i <= n:
        while n % i == 0:
            max_pf = i
            n //= i
        i += 1
    if n > 1:
        max_pf = max(max_pf, n)
    return max_pf


def func2(n: int) -> int:
    """Optimized trial division: remove factor 2, then test odd divisors only."""
    if n < 2:
        raise ValueError("n must be >= 2")
    max_pf = 1
    # Remove factors of 2
    while n % 2 == 0:
        max_pf = 2
        n //= 2
    # Test odd factors
    f = 3
    while f * f <= n:
        while n % f == 0:
            max_pf = f
            n //= f
        f += 2
    if n > 1:
        max_pf = max(max_pf, n)
    return max_pf


def _sieve_primes_up_to(limit: int) -> List[int]:
    if limit < 2:
        return []
    sieve = bytearray(b'\x01') * (limit + 1)
    sieve[0:2] = b'\x00\x00'
    for p in range(2, int(limit**0.5) + 1):
        if sieve[p]:
            step = p
            start = p*p
            sieve[start:limit+1:step] = b'\x00' * (((limit - start)//step) + 1)
    return [i for i, isprime in enumerate(sieve) if isprime]


def func3(n: int) -> int:
    """Use a prime sieve up to sqrt(n), divide by primes only."""
    if n < 2:
        raise ValueError("n must be >= 2")
    max_pf = 1
    limit = math.isqrt(n) + 1
    primes = _sieve_primes_up_to(limit)
    for p in primes:
        while n % p == 0:
            max_pf = p
            n //= p
        if n == 1:
            break
    # If remaining n > 1 it's prime (and larger than sieve limit)
    if n > 1:
        max_pf = max(max_pf, n)
    return max_pf


# --- For func4: Miller-Rabin (deterministic for 64-bit) + Pollard's Rho ---
def _is_probable_prime(n: int) -> bool:
    if n < 2:
        return False
    small_primes = (2, 3, 5, 7, 11, 13, 17, 19, 23, 29)
    for p in small_primes:
        if n % p == 0:
            return n == p
    # Write n-1 as d * 2^s
    d = n - 1
    s = 0
    while d % 2 == 0:
        d //= 2
        s += 1
    # Deterministic bases for testing 64-bit integers
    bases = (2, 325, 9375, 28178, 450775, 9780504, 1795265022)
    for a in bases:
        if a % n == 0:
            continue
        x = pow(a, d, n)
        if x == 1 or x == n - 1:
            continue
        composite = True
        for _ in range(s - 1):
            x = (x * x) % n
            if x == n - 1:
                composite = False
                break
        if composite:
            return False
    return True


def _pollards_rho(n: int) -> int:
    if n % 2 == 0:
        return 2
    if n % 3 == 0:
        return 3
    # f(x) = x^2 + c mod n
    while True:
        x = random.randrange(2, n - 1)
        y = x
        c = random.randrange(1, n - 1)
        d = 1
        while d == 1:
            x = (x * x + c) % n
            y = (y * y + c) % n
            y = (y * y + c) % n
            d = math.gcd(abs(x - y), n)
            if d == n:
                break
        if d > 1 and d < n:
            return d


def _factor_pollard(n: int, factors: List[int]):
    if n == 1:
        return
    if _is_probable_prime(n):
        factors.append(n)
        return
    d = _pollards_rho(n)
    _factor_pollard(d, factors)
    _factor_pollard(n // d, factors)


def func4(n: int) -> int:
    """Pollard's Rho factorization with Miller-Rabin primality check."""
    if n < 2:
        raise ValueError("n must be >= 2")
    factors: List[int] = []
    _factor_pollard(n, factors)
    return max(factors)


def func5(n: int) -> int:
    """Wheel (6k ± 1) trial division."""
    if n < 2:
        raise ValueError("n must be >= 2")
    # Remove factors 2 and 3
    max_pf = 1
    for p in (2, 3):
        while n % p == 0:
            max_pf = p
            n //= p
    # Test candidates of form 6k-1 and 6k+1
    k = 1
    while (6 * k - 1) * (6 * k - 1) <= n:
        for candidate in (6 * k - 1, 6 * k + 1):
            while n % candidate == 0:
                max_pf = candidate
                n //= candidate
        k += 1
    if n > 1:
        max_pf = max(max_pf, n)
    return max_pf

cot_gpt = [func1, func2, func3, func4, func5]