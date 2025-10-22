# FROM HUMANEVAL: https://huggingface.co/datasets/openai/openai_humaneval/viewer/openai_humaneval/test?views%5B%5D=test&row=8

from solutions import funcs
from pass_at_k_metric import pass_at_k

def check_unique(func):
    try:
        assert func([5, 3, 5, 2, 3, 3, 9, 0, 123]) == [0, 2, 3, 5, 9, 123]
    except AssertionError:
        return False

def test_funcs():
    for func in funcs:
        check_unique(func)

def test_pass_at_k():   
    score = pass_at_k(funcs, check_unique)
    assert score >= 0.5