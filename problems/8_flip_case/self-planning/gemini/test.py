# FROM HUMANEVAL: https://huggingface.co/datasets/openai/openai_humaneval/viewer/openai_humaneval/test?views%5B%5D=test&row=8

from solutions import funcs
from pass_at_k_metric import pass_at_k

def check_flip_case(func):
    try:
        assert func('') == ''
        assert func('Hello!') == 'hELLO!'
        assert func('These violent delights have violent ends') == 'tHESE VIOLENT DELIGHTS HAVE VIOLENT ENDS'
    except AssertionError:
        return False

def test_funcs():
    for func in funcs:
        check_flip_case(func)

def test_pass_at_k():   
    score = pass_at_k(funcs, check_flip_case)
    assert score >= 0.5