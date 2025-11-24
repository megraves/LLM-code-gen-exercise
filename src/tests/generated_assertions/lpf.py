# Domain assumptions
assert isinstance(n, int)
assert n > 1
assert not (  # n is not prime → has at least one composite factorization
    all(n % k != 0 for k in range(2, int(n**0.5) + 1))
)

# ans must be a positive integer
assert isinstance(ans, int)
assert ans > 1

# ans divides n
assert n % ans == 0

# ans is prime
assert all(ans % k != 0 for k in range(2, int(ans**0.5) + 1))

# ans is the largest prime divisor of n
for k in range(ans + 1, n + 1):
    assert not (n % k == 0 and all(k % d != 0 for d in range(2, int(k**0.5) + 1)))

# Any factor of n that is prime must be ≤ ans
for k in range(2, n + 1):
    if n % k == 0 and all(k % d != 0 for d in range(2, int(k**0.5) + 1)):
        assert k <= ans

# ans equals the maximum over all prime divisors of n
prime_divisors = [
    k for k in range(2, n + 1)
    if n % k == 0 and all(k % d != 0 for d in range(2, int(k**0.5) + 1))
]
assert ans == max(prime_divisors)

# ans appears in at least one valid prime factorization of n
# i.e., exists exponent e ≥ 1 with ans**e dividing n
assert any(n % (ans**e) == 0 for e in range(1, int(n**0.5) + 2))

# No larger composite factor can invalidate ans being prime
# (i.e., if a composite factor > ans exists, its prime factors must be ≤ ans)
for k in range(ans + 1, n + 1):
    if n % k == 0:
        # For any composite divisor k, all prime factors ≤ ans
        for p in range(2, k + 1):
            if k % p == 0 and all(p % d != 0 for d in range(2, int(p**0.5) + 1)):
                assert p <= ans
