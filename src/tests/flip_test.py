# import for testing pass@k metric
from .pass_at_k_metric import pass_at_k

# Import the generated functions to be tested
from ..problems.flip.scotgptcode import scot_gpt
from ..problems.flip.scotgeminicode import scot_gemini
from ..problems.flip.splangptcode import splan_gpt
from ..problems.flip.splangeminicode import splan_gemini

flip_code = [scot_gpt, scot_gemini, splan_gpt, splan_gemini]

def check_flip(func):
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

def test_flip():
    for funcs in flip_code:
        for func in funcs:
            check_flip(func)


def test_pass_at_k():   
    score1 = pass_at_k(scot_gpt, check_flip)
    score2 = pass_at_k(scot_gemini, check_flip)
    score3 = pass_at_k(splan_gpt, check_flip)
    score4 = pass_at_k(splan_gemini, check_flip)
    print(f"Pass@k score scot gpt: {score1}")
    print(f"Pass@k score scot gemini: {score2}")
    print(f"Pass@k score splan gpt: {score3}")
    print(f"Pass@k score splan gemini: {score4}")
    assert score1 >= 0.5
    assert score2 >= 0.5
    assert score3 >= 0.5
    assert score4 >= 0.5