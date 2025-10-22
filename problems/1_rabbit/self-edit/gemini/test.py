# FROM HUMANEVAL: https://huggingface.co/datasets/openai/openai_humaneval/viewer/openai_humaneval/test?views%5B%5D=test&row=8

from solutions import funcs
from pass_at_k_metric import pass_at_k

def check_rabbit(func):
    try:
        # Check some simple cases
        assert True, "This prints if this assert fails 1 (good for debugging!)"
        assert func(5, 6, 10) == [11, 4], "Error"
        assert func(4, 8, 9) == [12, 1], "Error"
        assert func(1, 10, 10) == [11, 0], "Error"
        assert func(2, 11, 5) == [7, 0], "Error"

        # Check some edge cases that are easy to work out by hand.
        assert True, "This prints if this assert fails 2 (also good for debugging!)"
        assert func(4, 5, 7) == [9, 2], "Error"
        assert func(4, 5, 1) == [5, 0], "Error"
        return True
    except AssertionError:
        return False
    except Exception:
        return False

def test_funcs():
    for func in funcs:
        check_rabbit(func)

def test_pass_at_k():   
    score = pass_at_k(funcs, check_rabbit)
    print(f"Pass@k score: {score}")
    assert score >= 0.5