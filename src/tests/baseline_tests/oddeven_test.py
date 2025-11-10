# import for testing pass@k metric
from ..pass_at_k_metric import pass_at_k

# Import the generated functions to be tested
from ...problems.oddeven.cotgptcode import cot_gpt
from ...problems.oddeven.cotgeminicode import cot_gemini
from ...problems.oddeven.sdebuggptcode import sdebug_gpt
from ...problems.oddeven.sdebuggeminicode import sdebug_gemini

oddeven_code = [cot_gpt, cot_gemini, sdebug_gpt, sdebug_gemini]

def check_oddeven(func):
    try:
        # Check some simple cases
        assert func([5, 8, 7, 1]) == 12
        assert func([3, 3, 3, 3, 3]) == 9
        assert func([30, 13, 24, 321]) == 0
        assert func([5, 9]) == 5
        assert func([2, 4, 8]) == 0
        assert func([30, 13, 23, 32]) == 23
        assert func([3, 13, 2, 9]) == 3
        return True
    except AssertionError:
        return False
    except Exception:
        return False

def test_oddeven():
    for funcs in oddeven_code:
        for func in funcs:
            check_oddeven(func)


def test_pass_at_k():   
    score1 = pass_at_k(cot_gpt, check_oddeven)
    score2 = pass_at_k(cot_gemini, check_oddeven)
    score3 = pass_at_k(sdebug_gpt, check_oddeven)
    score4 = pass_at_k(sdebug_gemini, check_oddeven)
    print(f"Pass@k score cot gpt: {score1}")
    print(f"Pass@k score cot gemini: {score2}")
    print(f"Pass@k score sdebug gpt: {score3}")
    print(f"Pass@k score sdebug gemini: {score4}")
    assert score1 >= 0.5
    assert score2 >= 0.5
    assert score3 >= 0.5
    assert score4 >= 0.5