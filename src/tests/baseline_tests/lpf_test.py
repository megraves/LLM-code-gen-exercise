# import for testing pass@k metric
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

        # Use assertions to print the failing case
        try: assert func(15) == 5
        except AssertionError: print("Failed on 15"); return False

        try: assert func(27) == 3
        except AssertionError: print("Failed on 27"); return False

        # ... and so on for all tests

        print(f"Function {func.__name__} PASSED.")
        return True
    except AssertionError:
        return False
    except Exception:
        return False

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