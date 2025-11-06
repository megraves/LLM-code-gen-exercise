import math

def func1(n: int) -> int:
    """Return the largest prime factor of n. Assume n > 1 and is not a prime.
    Method: Trial Division and Max Tracking (Optimized for 2, tracks largest)
    """
    largest_factor = 1
    temp_n = n

    # Check for factor 2 first
    if temp_n % 2 == 0:
        largest_factor = 2
        while temp_n % 2 == 0:
            temp_n //= 2

    # Check for odd factors
    i = 3
    # Check up to the square root of the *remaining* temp_n
    while i * i <= temp_n:
        if temp_n % i == 0:
            largest_factor = i
            while temp_n % i == 0:
                temp_n //= i
        i += 2

    # If temp_n > 1, the remaining value is the largest prime factor
    if temp_n > 1:
        largest_factor = temp_n

    return largest_factor


def func2(n: int) -> int:
    """Return the largest prime factor of n. Assume n > 1 and is not a prime.
    Method: Trial Division with sqrt(n) Limit and Factor List (returns max from list)
    """
    factors = []
    i = 2
    temp_n = n

    while i * i <= temp_n:
        if temp_n % i == 0:
            factors.append(i)
            # Repeatedly divide out the factor
            while temp_n % i == 0:
                temp_n //= i
        i += 1

    # If temp_n remains greater than 1, it's the largest prime factor
    if temp_n > 1:
        factors.append(temp_n)

    # The last factor added will be the largest
    return factors[-1]


def func3(n: int) -> int:
    """Return the largest prime factor of n. Assume n > 1 and is not a prime.
    Method: Optimized Trial Division with Early Exit (Most efficient iterative approach)
    """
    max_prime = 1
    temp_n = n
    
    # Handle factor 2
    if temp_n % 2 == 0:
        max_prime = 2
        while temp_n % 2 == 0:
            temp_n //= 2

    # Handle odd factors
    d = 3
    # Check up to sqrt(temp_n)
    while d * d <= temp_n:
        if temp_n % d == 0:
            max_prime = d
            while temp_n % d == 0:
                temp_n //= d
        d += 2

    # The remaining number is the largest prime factor if it's > 1
    if temp_n > 1:
        return temp_n
    
    return max_prime


def func4(n: int) -> int:
    """Return the largest prime factor of n. Assume n > 1 and is not a prime.
    Method: Prime Factor Sieve and Check (Generates primes up to sqrt(N) first)
    """
    limit = int(math.sqrt(n))
    
    # 1. Generate primes up to sqrt(n) using a basic sieve
    is_prime = [True] * (limit + 1)
    if limit >= 0: is_prime[0] = False
    if limit >= 1: is_prime[1] = False
    
    for p in range(2, int(math.sqrt(limit)) + 1):
        if is_prime[p]:
            for i in range(p * p, limit + 1, p):
                is_prime[i] = False
    
    primes = [p for p, is_p in enumerate(is_prime) if is_p]

    # 2. Check these primes against n
    largest_factor = 1
    temp_n = n

    for p in primes:
        if p * p > temp_n: 
             break
        
        if temp_n % p == 0:
            largest_factor = p
            while temp_n % p == 0:
                temp_n //= p

    # If temp_n is still > 1, it's the largest prime factor
    if temp_n > 1:
        return temp_n
    
    return largest_factor


def _get_smallest_factor(n: int) -> int:
    """Helper function: Finds the smallest factor of n, or n itself if prime."""
    if n % 2 == 0:
        return 2
    d = 3
    while d * d <= n:
        if n % d == 0:
            return d
        d += 2
    return n # n is prime

def func5(n: int) -> int:
    """Return the largest prime factor of n. Assume n > 1 and is not a prime.
    Method: Recursive Factorization (Inefficient due to function calls)
    """
    # Find the smallest prime factor
    smallest_factor = _get_smallest_factor(n)
    
    # Base case: if smallest_factor is n, n is prime
    if smallest_factor == n: 
        return n
    
    # Recursive step: Find the largest prime factor of the reduced number (n // smallest_factor)
    return func5(n // smallest_factor)

cot_gemini = [func1, func2, func3, func4, func5]