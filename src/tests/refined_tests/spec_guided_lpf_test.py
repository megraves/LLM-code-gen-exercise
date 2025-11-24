import pytest
import math

# Add imports for the lpf functions to be tested
from ...problems.lpf.cotgptcode import cot_gpt
from ...problems.lpf.cotgeminicode import cot_gemini
from ...problems.lpf.srepairgptcode import srepair_gpt
from ...problems.lpf.srepairgeminicode import srepair_gemini

lpf_code = [cot_gpt, cot_gemini, srepair_gpt, srepair_gemini]

# ---- Helper: primality test used only for validating specifications ----
def is_prime(x: int) -> bool:
    if x < 2:
        return False
    for k in range(2, int(math.sqrt(x)) + 1):
        if x % k == 0:
            return False
    return True


# ---- Shared specification checker ----
def check_specs(n: int, ans: int):
    # ans must be a positive integer > 1
    assert isinstance(ans, int)
    assert ans > 1

    # ans divides n
    assert n % ans == 0

    # ans is prime
    assert is_prime(ans)

    # ans is the largest prime divisor of n
    for k in range(ans + 1, n + 1):
        if n % k == 0 and is_prime(k):
            pytest.fail(f"{k} is a larger prime divisor than ans={ans}")

    # Any prime factor of n must be ≤ ans
    for k in range(2, n + 1):
        if n % k == 0 and is_prime(k):
            assert k <= ans


# ---- Tests ----
@pytest.mark.parametrize("n", [
    4,          # 2^2 → largest PF = 2
    6,          # 2 * 3 → largest PF = 3
    8,          # 2^3 → largest PF = 2
    10,         # 2 * 5 → largest PF = 5
    12,         # 2^2 * 3 → largest PF = 3
    15,         # 3 * 5 → largest PF = 5
    21,         # 3 * 7 → largest PF = 7
    25,         # 5^2 → largest PF = 5
    27,         # 3^3 → largest PF = 3
    45,         # 3^2 * 5 → largest PF = 5
    49,         # 7^2 → largest PF = 7
    77,         # 7 * 11 → largest PF = 11
    84,         # includes 7 → LPF = 7
    100,        # 2^2 * 5^2 → LPF = 5
    13195,      # known PF set: {5,7,13,29} → LPF = 29
])
def test_lpf_specifications(n):
    # added the loop to test all implementations of lpf
    for funcs in lpf_code:
        for func in funcs:
            ans = func(n)
            check_specs(n, ans)