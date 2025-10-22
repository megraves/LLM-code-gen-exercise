# FROM HUMANEVAL: https://huggingface.co/datasets/openai/openai_humaneval/viewer/openai_humaneval/test?views%5B%5D=test&row=8

from solutions import funcs
from pass_at_k_metric import pass_at_k

def check_sum_prod(func):
    try:
        assert func([]) == (0, 1)
        assert func([1, 1, 1]) == (3, 1)
        assert func([100, 0]) == (100, 0)
        assert func([3, 5, 7]) == (3 + 5 + 7, 3 * 5 * 7)
        assert func([10]) == (10, 10)
    except AssertionError:
        return False

def test_funcs():
    for func in funcs:
        check_sum_prod(func)

def test_pass_at_k():   
    score = pass_at_k(funcs, check_sum_prod)
    assert score >= 0.5