# From humaneval: https://huggingface.co/datasets/openai/openai_humaneval/viewer/openai_humaneval/test?p=1&views%5B%5D=test&row=121

from solutions import funcs
from pass_at_k_metric import pass_at_k

def check_odd_n_even(func):
    try:
        # Check some simple cases
        assert func([5, 8, 7, 1]) == 12
        assert func([3, 3, 3, 3, 3]) == 9
        assert func([30, 13, 24, 321]) == 0
        assert func([5, 9]) == 5
        assert func([2, 4, 8]) == 0
        assert func([30, 13, 23, 32]) == 23
        assert func([3, 13, 2, 9]) == 3
    except AssertionError:
        return False

def test_funcs():
    for func in funcs:
        check_odd_n_even(func)

def test_pass_at_k():   
    score = pass_at_k(funcs, check_odd_n_even)
    assert score >= 0.5