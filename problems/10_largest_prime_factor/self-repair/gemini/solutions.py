import math

def func1(n: int) -> int:
    """
    Solution 1: Standard Optimized Trial Division.
    The most common and efficient iterative approach.
    It removes factors as it finds them, ensuring the remaining value is always composite or prime.
    It checks 2 separately, then iterates only over odd numbers.
    """
    largest_prime = 1
    
    # 1. Handle factor 2
    if n % 2 == 0:
        largest_prime = 2
        while n % 2 == 0:
            n //= 2

    # 2. Iterate over odd factors up to sqrt(n)
    i = 3
    # Note: We check up to sqrt(n) of the remaining n
    while i * i <= n:
        if n % i == 0:
            largest_prime = i
            # Divide n by the factor until it's no longer divisible
            while n % i == 0:
                n //= i
        i += 2

    # 3. Handle the case where the remaining n is prime (and the largest factor)
    if n > 2:
        largest_prime = n

    return largest_prime

def func2(n: int) -> int:
    """
    Solution 2: Less Optimized Trial Division using a factor list.
    This approach finds all prime factors first, stores them, and then returns the maximum.
    It is conceptually similar to func1 but uses a list which is less space-efficient for very large N.
    """
    n_copy = n
    factors = []
    
    # Handle factor 2
    if n_copy % 2 == 0:
        factors.append(2)
        while n_copy % 2 == 0:
            n_copy //= 2

    # Iterate over odd factors
    i = 3
    limit = int(math.sqrt(n_copy)) + 1
    while i < limit:
        if n_copy % i == 0:
            factors.append(i)
            while n_copy % i == 0:
                n_copy //= i
            # Recalculate limit because n_copy has been reduced
            limit = int(math.sqrt(n_copy)) + 1
        i += 2

    # If the remaining number is greater than 2, it is the largest prime factor
    if n_copy > 2:
        factors.append(n_copy)

    # Return the largest factor found
    return max(factors) if factors else 1


def _find_smallest_factor(k: int) -> int:
    """Helper function to find the smallest factor (>= 2) of k."""
    if k % 2 == 0:
        return 2
    i = 3
    while i * i <= k:
        if k % i == 0:
            return i
        i += 2
    return k # k is prime

def func3(n: int) -> int:
    """
    Solution 3: Recursive Factorization.
    This approach recursively finds the smallest prime factor, and then calls itself 
    on the quotient, returning the maximum prime found at any step.
    """
    if n <= 1:
        return 1
    
    # Find the smallest prime factor (f) of n
    f = _find_smallest_factor(n)
    
    # If n is prime (f == n), return n
    if f == n:
        return n
    
    # If n is composite, the largest prime factor is max(f, largest_prime_factor(n/f))
    # Since we are recursively finding the factors of n/f, the largest factor will eventually bubble up.
    
    # Example: largest_prime_factor(13195)
    # f = 5. largest_prime_factor(2639)
    #   f = 11. largest_prime_factor(239)
    #     f = 239 (prime). returns 239.
    #   returns max(11, 239) = 239.
    # returns max(5, 239) = 239.
    
    return func3(n // f)

def func4(n: int) -> int:
    """
    Solution 4: Trial Division with 6k +/- 1 Optimization.
    Any prime number greater than 3 can be expressed as 6k-1 or 6k+1.
    This avoids checking multiples of 2 and 3 (like 5, 7, 11, 13, 17, 19...).
    """
    largest_prime = 1
    
    n_copy = n
    
    # Handle factors 2 and 3
    for f in [2, 3]:
        if n_copy % f == 0:
            largest_prime = f
            while n_copy % f == 0:
                n_copy //= f

    # Check factors from 5 onwards using the 6k +/- 1 pattern
    i = 5
    while i * i <= n_copy:
        # Check i (6k - 1)
        if n_copy % i == 0:
            largest_prime = i
            while n_copy % i == 0:
                n_copy //= i
        
        # Check i + 2 (6k + 1)
        if n_copy % (i + 2) == 0:
            largest_prime = i + 2
            while n_copy % (i + 2) == 0:
                n_copy //= (i + 2)
        
        # Increment to the next pair (e.g., 5 -> 11)
        i += 6

    # The remaining n_copy is the largest prime factor if it's > 4
    if n_copy > 4:
        largest_prime = n_copy

    return largest_prime

def func5(n: int) -> int:
    """
    Solution 5: Pre-calculate Primes up to sqrt(n) using Sieve and check in reverse.
    This is less efficient for a single large N, but conceptually distinct as it pre-computes primality.
    """
    limit = int(math.sqrt(n)) + 1
    
    # 1. Sieve of Eratosthenes to find all primes up to the square root of n
    is_prime = [True] * limit
    primes = []
    
    for p in range(2, limit):
        if is_prime[p]:
            primes.append(p)
            for i in range(p * p, limit, p):
                is_prime[i] = False
                
    # 2. Check the original number n against primes in reverse order
    # The first prime that divides n from the back is the largest prime factor.
    # We must also handle the case where n has a prime factor > limit.

    # First, check for factors from the pre-calculated list
    largest_factor_from_sieve = 1
    remaining_n = n

    for p in primes:
        if remaining_n % p == 0:
            largest_factor_from_sieve = p
            # While dividing, ensure we remove all instances of p
            while remaining_n % p == 0:
                remaining_n //= p

    # 3. If remaining_n is greater than 1, it must be the single largest prime factor
    if remaining_n > 1:
        return remaining_n
    
    # Otherwise, the largest factor found by the sieve is the answer
    return largest_factor_from_sieve

funcs = [func1, func2, func3, func4, func5]