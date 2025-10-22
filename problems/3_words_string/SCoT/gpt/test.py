#From humaneval: https://huggingface.co/datasets/openai/openai_humaneval/viewer/openai_humaneval/test?p=1&views%5B%5D=test&row=101
from solutions import funcs
from pass_at_k_metric import pass_at_k

def check_word_string(func):
    try:
     # Check some simple cases
        assert True, "This prints if this assert fails 1 (good for debugging!)"
        assert func("Hi, my name is John") == ["Hi", "my", "name", "is", "John"]
        assert func("One, two, three, four, five, six") == ["One", "two", "three", "four", "five", "six"]
        assert func("Hi, my name") == ["Hi", "my", "name"]
        assert func("One,, two, three, four, five, six,") == ["One", "two", "three", "four", "five", "six"]

        # Check some edge cases that are easy to work out by hand.
        assert True, "This prints if this assert fails 2 (also good for debugging!)"
        assert func("") == []
        assert func("ahmed , gamal") == ["ahmed", "gamal"]

    except AssertionError:
        return False

def test_funcs():
    for func in funcs:
        check_word_string(func)

def test_pass_at_k():   
    score = pass_at_k(funcs, check_word_string)
    assert score >= 0.5