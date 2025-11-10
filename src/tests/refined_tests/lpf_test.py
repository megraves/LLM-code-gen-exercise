# import for testing pass@k metric
import pytest
from ..pass_at_k_metric import pass_at_k

# Import the generated functions to be tested
from ...problems.lpf.cotgptcode import cot_gpt
from ...problems.lpf.cotgeminicode import cot_gemini
from ...problems.lpf.srepairgptcode import srepair_gpt
from ...problems.lpf.srepairgeminicode import srepair_gemini

lpf_code = [cot_gpt, cot_gemini, srepair_gpt, srepair_gemini]

def check_lpf(func):
    try:
        # Add a print statement to see the function being tested
        print(f"Testing function: {func.__name__}")

        # Edge cases omitted by AI that I added
        with pytest.raises(ValueError, match="n must be >= 2"):
            func(0)
        with pytest.raises(ValueError, match="n must be >= 2"):
            func(-1)
        with pytest.raises(ValueError, match="n must be >= 2"):
            func(1)

        # --- Existing Tests (Good for basic coverage) ---
        try: assert func(15) == 5
        except AssertionError: print("Failed on 15. Expected 5"); raise

        try: assert func(27) == 3
        except AssertionError: print("Failed on 27. Expected 3"); raise
        
        try: assert func(13195) == 29  # From docstring
        except AssertionError: print("Failed on 13195. Expected 29"); raise

        try: assert func(2048) == 2    # From docstring
        except AssertionError: print("Failed on 2048. Expected 2"); raise

        # --- New Tests for Increased Coverage ---
        
        # Power of 2 (Smallest prime)
        try: assert func(8) == 2
        except AssertionError: print("Failed on 8. Expected 2"); raise

        # Simple mix (2 * 5)
        try: assert func(10) == 5
        except AssertionError: print("Failed on 10. Expected 5"); raise

        # Larger prime factor (3 * 17)
        try: assert func(51) == 17
        except AssertionError: print("Failed on 51. Expected 17"); raise

        # Square of a prime (7 * 7)
        try: assert func(49) == 7
        except AssertionError: print("Failed on 49. Expected 7"); raise

        # Mix of small and larger prime (3^2 * 11)
        try: assert func(99) == 11
        except AssertionError: print("Failed on 99. Expected 11"); raise
        
        # Two larger factors (11 * 89)
        try: assert func(979) == 89
        except AssertionError: print("Failed on 979. Expected 89"); raise
        
        # Very large power of 2
        try: assert func(1024) == 2
        except AssertionError: print("Failed on 1024. Expected 2"); raise

        # --- Final Edge Cases (NEW) ---
        # Smallest composite number (2^2)
        try: assert func(4) == 2
        except AssertionError: print("Failed on 4. Expected 2"); raise
        
        # Smallest odd power of a prime (3^2)
        try: assert func(9) == 3
        except AssertionError: print("Failed on 9. Expected 3"); raise
        
        # --- Base & Docstring Tests ---
        try: assert func(15) == 5
        except AssertionError: print("Failed on 15. Expected 5"); raise
        try: assert func(27) == 3
        except AssertionError: print("Failed on 27. Expected 3"); raise
        try: assert func(13195) == 29
        except AssertionError: print("Failed on 13195. Expected 29"); raise
        try: assert func(2048) == 2
        except AssertionError: print("Failed on 2048. Expected 2"); raise

        # --- Intermediate Coverage Tests ---
        try: assert func(8) == 2
        except AssertionError: print("Failed on 8. Expected 2"); raise
        try: assert func(10) == 5
        except AssertionError: print("Failed on 10. Expected 5"); raise
        try: assert func(51) == 17
        except AssertionError: print("Failed on 51. Expected 17"); raise
        try: assert func(49) == 7
        except AssertionError: print("Failed on 49. Expected 7"); raise
        try: assert func(99) == 11
        except AssertionError: print("Failed on 99. Expected 11"); raise
        try: assert func(979) == 89
        except AssertionError: print("Failed on 979. Expected 89"); raise
        try: assert func(1024) == 2
        except AssertionError: print("Failed on 1024. Expected 2"); raise
        
        # --- Extreme Coverage Tests ---
        try: assert func(600) == 5
        except AssertionError: print("Failed on 600. Expected 5"); raise
        try: assert func(4913) == 17
        except AssertionError: print("Failed on 4913. Expected 17"); raise
        try: assert func(82100) == 821
        except AssertionError: print("Failed on 82100. Expected 821"); raise

        print(f"Function {func.__name__} PASSED.")
        return True
    except AssertionError as e:
        # Catch assertion error if something unexpected happens outside the try blocks
        raise e
    except Exception as e:
        # Catch general errors (e.g., infinite loop, type error)
        print(f"Function {func.__name__} FAILED with an exception: {e}")
        raise e

def test_lpf():
    for funcs in lpf_code:
        for func in funcs:
            check_lpf(func)


def test_pass_at_k():   
    score1 = pass_at_k(cot_gpt, check_lpf)
    score2 = pass_at_k(cot_gemini, check_lpf)
    score3 = pass_at_k(srepair_gpt, check_lpf)
    score4 = pass_at_k(srepair_gemini, check_lpf)
    print(f"Pass@k score cot gpt: {score1}")
    print(f"Pass@k score cot gemini: {score2}")
    print(f"Pass@k score srepair gpt: {score3}")
    print(f"Pass@k score srepair gemini: {score4}")
    assert score1 >= 0.5
    assert score2 >= 0.5
    assert score3 >= 0.5
    assert score4 >= 0.5