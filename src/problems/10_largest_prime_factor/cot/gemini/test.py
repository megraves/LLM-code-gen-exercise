# FROM HUMANEVAL: https://huggingface.co/datasets/openai/openai_humaneval/viewer/openai_humaneval/test?views%5B%5D=test&row=8

from solutions import funcs
from pass_at_k_metric import pass_at_k

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
        return True # Explicitly return True on success

    except Exception as e:
        # Catch other exceptions like TypeError
        print(f"Function {func.__name__} raised exception: {e}")
        return False

def test_funcs():
    for func in funcs:
        check_lpf(func)

def test_pass_at_k():   
    score = pass_at_k(funcs, check_lpf)
    print(f"The pass@k score is: {score}")
    assert score >= 0.5