import pytest
from typing import List

# Add imports for the rescale function to be tested
from ...problems.rescale.scotgptcode import scot_gpt
from ...problems.rescale.scotgeminicode import scot_gemini
from ...problems.rescale.seditgptcode import sedit_gpt
from ...problems.rescale.seditgeminicode import sedit_gemini

rescale_code = [scot_gpt, scot_gemini, sedit_gpt, sedit_gemini]

# Add to test all functions in rescale_code
def test_all():
    for funcs in rescale_code:
        for func in funcs:
            test_standard_positive(func)
            test_negative_numbers(func)
            test_all_elements_same(func)
            test_two_elements(func)
            test_includes_zero(func)
            test_close_numbers(func)

# --- Test Functions ---

# Test 1: Standard case with distinct positive floats
def test_standard_positive(rescale):
    numbers = [10.0, 20.0, 30.0, 15.0]
    ans = rescale(numbers)
    
    # Assertions based on specifications
    assert len(ans) == len(numbers)
    assert pytest.approx(min(ans)) == 0.0
    # max(ans) should be 1.0 when numbers are not all equal
    assert pytest.approx(max(ans)) == 1.0 
    assert all(0.0 <= x <= 1.0 for x in ans)
    
    # Specific transformation check (part of the original spec's logic)
    min_val = 10.0
    max_val = 30.0
    range_val = 20.0
    
    expected = [
        (10.0 - min_val) / range_val,  # 0.0
        (20.0 - min_val) / range_val,  # 0.5
        (30.0 - min_val) / range_val,  # 1.0
        (15.0 - min_val) / range_val,  # 0.25
    ]
    assert all(
        abs(ans[i] - expected[i]) < 1e-9
        for i in range(len(numbers))
    )

# Test 2: Case with negative numbers
def test_negative_numbers(rescale):
    numbers = [-10.0, 0.0, 5.0, -5.0]
    ans = rescale(numbers)
    
    assert len(ans) == len(numbers)
    assert pytest.approx(min(ans)) == 0.0
    assert pytest.approx(max(ans)) == 1.0
    assert all(0.0 <= x <= 1.0 for x in ans)

    # Specific transformation check
    min_val = -10.0
    max_val = 5.0
    range_val = 15.0 # 5.0 - (-10.0)
    
    expected = [
        (-10.0 - min_val) / range_val, # 0.0
        (0.0 - min_val) / range_val,   # 10.0 / 15.0
        (5.0 - min_val) / range_val,   # 1.0
        (-5.0 - min_val) / range_val,  # 5.0 / 15.0
    ]
    assert all(
        abs(ans[i] - expected[i]) < 1e-9
        for i in range(len(numbers))
    )

# Test 3: Edge case where all numbers are the same (constant list)
def test_all_elements_same(rescale):
    numbers = [5.5, 5.5, 5.5, 5.5]
    ans = rescale(numbers)
    
    assert len(ans) == len(numbers)
    assert pytest.approx(min(ans)) == 0.0
    
    # The specification requires max(ans) == 0.0 if all numbers are the same
    assert len(set(numbers)) == 1 and pytest.approx(max(ans)) == 0.0
    assert all(0.0 <= x <= 1.0 for x in ans)
    
    # Additional required check for constant list
    assert ans == [0.0, 0.0, 0.0, 0.0] # Should be [0.0] * len(numbers)

# Test 4: List with only two elements (minimum length requirement)
def test_two_elements(rescale):
    numbers = [42.0, 100.0]
    ans = rescale(numbers)
    
    assert len(ans) == len(numbers)
    assert pytest.approx(min(ans)) == 0.0
    assert pytest.approx(max(ans)) == 1.0
    assert all(0.0 <= x <= 1.0 for x in ans)
    
    # Specific transformation check
    assert pytest.approx(ans[0]) == 0.0
    assert pytest.approx(ans[1]) == 1.0

# Test 5: List including 0.0
def test_includes_zero(rescale):
    numbers = [0.0, 5.0, 10.0, -5.0]
    ans = rescale(numbers)
    
    assert len(ans) == len(numbers)
    assert pytest.approx(min(ans)) == 0.0
    assert pytest.approx(max(ans)) == 1.0
    assert all(0.0 <= x <= 1.0 for x in ans)
    
    # Specific transformation check
    min_val = -5.0
    max_val = 10.0
    range_val = 15.0
    
    expected = [
        (0.0 - min_val) / range_val,   # 5/15
        (5.0 - min_val) / range_val,   # 10/15
        (10.0 - min_val) / range_val,  # 1.0
        (-5.0 - min_val) / range_val,  # 0.0
    ]
    assert all(
        abs(ans[i] - expected[i]) < 1e-9
        for i in range(len(numbers))
    )

# Test 6: Test with numbers that are very close to each other (precision check)
def test_close_numbers(rescale):
    numbers = [1.000000000000001, 1.000000000000002, 1.000000000000000]
    ans = rescale(numbers)
    
    assert len(ans) == len(numbers)
    assert pytest.approx(min(ans)) == 0.0
    assert pytest.approx(max(ans)) == 1.0
    assert all(0.0 <= x <= 1.0 for x in ans)
    
    # Specific transformation check (using the 1e-9 tolerance from the spec)
    min_val = numbers[2] # 1.000000000000000
    max_val = numbers[1] # 1.000000000000002
    range_val = max_val - min_val
    
    assert all(
        abs(ans[i] - (numbers[i] - min_val) / range_val) < 1e-9
        for i in range(len(numbers))
    )