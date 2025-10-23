
# Given a list of functions
# funcs: [func1, func2, ..., funcN]
# test: function that tests the correctness of each func
# k: number of attempts considered for success (this will be 3)
# n: number of functions in funcs (this will be 5)
# c: number of functions that pass the test
k = 3

import math

def pass_at_k(funcs, test):

    if k <= 0:
        return 0.0

    n = len(funcs)
    if n == 0:
        print("n is 0")
        return 0.0

    # Count correct implementations.
    c = 0.0
    for func in funcs:
        try:
            if test(func):
                c += 1.0
        except Exception:
            # Treat thrown exceptions as failing the test.
            # Optionally log the exception for debugging.
            continue

    # If none pass, probability is 0.
    if c == 0.0:
        print("none pass")
        return 0.0

    # If k > n-c then C(n-c, k) = 0 (no way to choose k wrong-only items),
    # so pass@k = 1.0 (because every k-subset must include at least one correct).
    if k > (n - c):
        return 1.0

    # Otherwise apply the combinatorial formula.
    numerator = math.comb(n - c, k)
    denominator = math.comb(n, k)
    metric = 1.0 - (numerator / denominator)
    print(metric)
    return metric