#From humaneval: https://huggingface.co/datasets/openai/openai_humaneval/viewer/openai_humaneval/test?p=1&views%5B%5D=test&row=100
from solutions import funcs
from pass_at_k_metric import pass_at_k

def check_stones(func):
    try:
        # Check some simple cases
        assert func(3) == [3, 5, 7], "Test 3"
        assert func(4) == [4,6,8,10], "Test 4"
        assert func(5) == [5, 7, 9, 11, 13]
        assert func(6) == [6, 8, 10, 12, 14, 16]
        assert func(8) == [8, 10, 12, 14, 16, 18, 20, 22]

        # Check some edge cases that are easy to work out by hand.
        assert True, "This prints if this assert fails 2 (also good for debugging!)"
        return True
    except AssertionError:
        return False
    except Exception:
        return False

def test_funcs():
    for func in funcs:
        check_stones(func)

def test_pass_at_k():   
    score = pass_at_k(funcs, check_stones)
    print(f"Pass@k score: {score}")
    assert score >= 0.5