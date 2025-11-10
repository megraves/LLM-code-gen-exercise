# import for testing pass@k metric
from ..pass_at_k_metric import pass_at_k

# Import the generated functions to be tested
from ...problems.stones.cotgptcode import cot_gpt
from ...problems.stones.cotgeminicode import cot_gemini
from ...problems.stones.sdebuggptcode import sdebug_gpt
from ...problems.stones.sdebuggeminicode import sdebug_gemini

stones_code = [cot_gpt, cot_gemini, sdebug_gpt, sdebug_gemini]

def check_stones(func):
    try:
        # Check some simple cases
        assert func(3) == [3, 5, 7], "Test 3"
        assert func(4) == [4,6,8,10], "Test 4"
        assert func(5) == [5, 7, 9, 11, 13]
        assert func(6) == [6, 8, 10, 12, 14, 16]
        assert func(8) == [8, 10, 12, 14, 16, 18, 20, 22]
        return True
    except AssertionError:
        return False
    except Exception:
        return False

def test_stones():
    for funcs in stones_code:
        for func in funcs:
            check_stones(func)


def test_pass_at_k():   
    score1 = pass_at_k(cot_gpt, check_stones)
    score2 = pass_at_k(cot_gemini, check_stones)
    score3 = pass_at_k(sdebug_gpt, check_stones)
    score4 = pass_at_k(sdebug_gemini, check_stones)
    print(f"Pass@k score cot gpt: {score1}")
    print(f"Pass@k score cot gemini: {score2}")
    print(f"Pass@k score sdebug gpt: {score3}")
    print(f"Pass@k score sdebug gemini: {score4}")
    assert score1 >= 0.5
    assert score2 >= 0.5
    assert score3 >= 0.5
    assert score4 >= 0.5