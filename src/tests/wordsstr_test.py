# import for testing pass@k metric
from .pass_at_k_metric import pass_at_k

# Import the generated functions to be tested
from ..problems.wordsstr.scotgptcode import scot_gpt
from ..problems.wordsstr.scotgeminicode import scot_gemini
from ..problems.wordsstr.splangptcode import splan_gpt
from ..problems.wordsstr.splangeminicode import splan_gemini

wordsstr_code = [scot_gpt, scot_gemini, splan_gpt, splan_gemini]

def check_wordsstr(func):
    try:
        # Check some simple cases
        assert True, "This prints if this assert fails 1"
        assert func("Hi, my name is John") == ["Hi", "my", "name", "is", "John"]
        assert func("One, two, three, four, five, six") == ["One", "two", "three", "four", "five", "six"]
        assert func("Hi, my name") == ["Hi", "my", "name"]
        assert func("One,, two, three, four, five, six,") == ["One", "two", "three", "four", "five", "six"]

        # Check some edge cases that are easy to work out by hand.
        assert True, "This prints if this assert fails 2"
        assert func("") == []
        assert func("ahmed , gamal") == ["ahmed", "gamal"]
        return True
    except AssertionError:
        return False
    except Exception:
        return False

def test_wordsstr():
    for funcs in wordsstr_code:
        for func in funcs:
            check_wordsstr(func)


def test_pass_at_k():   
    score1 = pass_at_k(scot_gpt, check_wordsstr)
    score2 = pass_at_k(scot_gemini, check_wordsstr)
    score3 = pass_at_k(splan_gpt, check_wordsstr)
    score4 = pass_at_k(splan_gemini, check_wordsstr)
    print(f"Pass@k score scot gpt: {score1}")
    print(f"Pass@k score scot gemini: {score2}")
    print(f"Pass@k score splan gpt: {score3}")
    print(f"Pass@k score splan gemini: {score4}")
    assert score1 >= 0.5
    assert score2 >= 0.5
    assert score3 >= 0.5
    assert score4 >= 0.5