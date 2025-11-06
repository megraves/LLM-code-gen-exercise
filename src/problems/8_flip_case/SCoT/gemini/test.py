# FROM HUMANEVAL: https://huggingface.co/datasets/openai/openai_humaneval/viewer/openai_humaneval/test?views%5B%5D=test&row=8

from solutions import funcs
from pass_at_k_metric import pass_at_k

def check_flip_case(func):
    try:
        assert func('') == ''
        assert func('Hello!') == 'hELLO!'
        assert func('These violent delights have violent ends') == 'tHESE VIOLENT DELIGHTS HAVE VIOLENT ENDS'
        assert func('all lowercase') == 'ALL LOWERCASE'
        assert func('ALL UPPERCASE') == 'all uppercase'
        assert func('123-abc-999') == '123-ABC-999'
        return True
    except AssertionError:
        return False
    except Exception:
        return False

def test_funcs():
    for func in funcs:
        check_flip_case(func)

def test_pass_at_k():   
    score = pass_at_k(funcs, check_flip_case)
    print(f"Pass@k score: {score}")
    assert score >= 0.5