# FROM HUMANEVAL: https://huggingface.co/datasets/openai/openai_humaneval/viewer/openai_humaneval/test?views%5B%5D=test&row=8

from solutions import funcs
from pass_at_k_metric import pass_at_k

def check_lpf(func):
    try:
        assert func(15) == 5
        assert func(27) == 3
        assert func(63) == 7
        assert func(330) == 11
        assert func(13195) == 29
    except AssertionError:
        return False

def test_funcs():
    for func in funcs:
        check_lpf(func)

def test_pass_at_k():   
    score = pass_at_k(funcs, check_lpf)
    assert score >= 0.5