# import for testing pass@k metric
from .pass_at_k_metric import pass_at_k

# Import the generated functions to be tested
from ..problems.substr.scotgptcode import scot_gpt
from ..problems.substr.scotgeminicode import scot_gemini
from ..problems.substr.srepairgptcode import srepair_gpt
from ..problems.substr.srepairgeminicode import srepair_gemini

substr_code = [scot_gpt, scot_gemini, srepair_gpt, srepair_gemini]

def check_substr(func):
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
    except Exception:
        return False

def test_substr():
    for funcs in substr_code:
        for func in funcs:
            check_substr(func)


def test_pass_at_k():   
    score1 = pass_at_k(scot_gpt, check_substr)
    score2 = pass_at_k(scot_gemini, check_substr)
    score3 = pass_at_k(srepair_gpt, check_substr)
    score4 = pass_at_k(srepair_gemini, check_substr)
    print(f"Pass@k score scot gpt: {score1}")
    print(f"Pass@k score scot gemini: {score2}")
    print(f"Pass@k score srepair gpt: {score3}")
    print(f"Pass@k score srepair gemini: {score4}")
    assert score1 >= 0.5
    assert score2 >= 0.5
    assert score3 >= 0.5
    assert score4 >= 0.5