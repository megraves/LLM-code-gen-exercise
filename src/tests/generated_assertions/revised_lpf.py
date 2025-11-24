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