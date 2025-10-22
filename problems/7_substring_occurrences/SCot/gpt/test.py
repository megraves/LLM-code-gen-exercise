# From humaneval: https://huggingface.co/datasets/openai/openai_humaneval/viewer/openai_humaneval/test?views%5B%5D=test&row=18
from solutions import funcs
from pass_at_k_metric import pass_at_k

def check_substring_occurrences(func):
    try:
        assert func('', 'x') == 0
        assert func('xyxyxyx', 'x') == 4
        assert func('cacacacac', 'cac') == 4
        assert func('john doe', 'john') == 1
        # Add my own test out of curiosity
        assert func('xxxx', 'xx') == 3
        return True
    except AssertionError:
        return False

def test_funcs():
    for func in funcs:
        check_substring_occurrences(func)

def test_pass_at_k():   
    score = pass_at_k(funcs, check_substring_occurrences)
    assert score >= 0.5