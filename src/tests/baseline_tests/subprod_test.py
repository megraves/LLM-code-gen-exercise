# import for testing pass@k metric
from ..pass_at_k_metric import pass_at_k

# Import the generated functions to be tested
from ...problems.sumprod.cotgptcode import cot_gpt
from ...problems.sumprod.cotgeminicode import cot_gemini
from ...problems.sumprod.seditgptcode import sedit_gpt
from ...problems.sumprod.seditgeminicode import sedit_gemini

sumprod_code = [cot_gpt, cot_gemini, sedit_gpt, sedit_gemini]

def check_sumprod(func):
    try:
        assert func([]) == (0, 1)
        assert func([1, 1, 1]) == (3, 1)
        assert func([100, 0]) == (100, 0)
        assert func([3, 5, 7]) == (3 + 5 + 7, 3 * 5 * 7)
        assert func([10]) == (10, 10)
        return True
    except AssertionError:
        return False
    except Exception:
        return False

def test_sumprod():
    for funcs in sumprod_code:
        for func in funcs:
            check_sumprod(func)


def test_pass_at_k():   
    score1 = pass_at_k(cot_gpt, check_sumprod)
    score2 = pass_at_k(cot_gemini, check_sumprod)
    score3 = pass_at_k(sedit_gpt, check_sumprod)
    score4 = pass_at_k(sedit_gemini, check_sumprod)
    print(f"Pass@k score cot gpt: {score1}")
    print(f"Pass@k score cot gemini: {score2}")
    print(f"Pass@k score sedit gpt: {score3}")
    print(f"Pass@k score sedit gemini: {score4}")
    assert score1 >= 0.5
    assert score2 >= 0.5
    assert score3 >= 0.5
    assert score4 >= 0.5