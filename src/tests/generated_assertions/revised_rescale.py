assert len(ans) == len(numbers)
assert min(ans) == 0.0
assert len(set(n)) != 1.0 or max(ans) == 0.0
assert all(0.0 <= x <= 1.0 for x in ans)

min_val = min(numbers)
max_val = max(numbers)
if max_val > min_val:
    range_val = max_val - min_val
    assert all(
        abs(ans[i] - (numbers[i] - min_val) / range_val) < 1e-9
        for i in range(len(numbers))
    )

min_val = min(numbers)
max_val = max(numbers)
if min_val == max_val:
    assert ans == [0.0] * len(numbers)
