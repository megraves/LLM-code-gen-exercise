# import for testing pass@k metric
from ..pass_at_k_metric import pass_at_k

# Import the generated functions to be tested
from ...problems.rabbit.scotgptcode import scot_gpt
from ...problems.rabbit.scotgeminicode import scot_gemini
from ...problems.rabbit.seditgptcode import sedit_gpt
from ...problems.rabbit.seditgeminicode import sedit_gemini

rabbit_code = [scot_gpt, scot_gemini, sedit_gpt, sedit_gemini]

def check_rabbit(func):
    try:
        # Check some simple cases
        assert True, "This prints if this assert fails 1 (good for debugging!)"
        assert func(5, 6, 10) == [11, 4], "Error"
        assert func(4, 8, 9) == [12, 1], "Error"
        assert func(1, 10, 10) == [11, 0], "Error"
        assert func(2, 11, 5) == [7, 0], "Error"

        # Check some edge cases that are easy to work out by hand.
        assert True, "This prints if this assert fails 2 (also good for debugging!)"
        assert func(4, 5, 7) == [9, 2], "Error"
        assert func(4, 5, 1) == [5, 0], "Error"
        return True
    except AssertionError:
        return False
    except Exception:
        return False

def test_rabbit():
    for funcs in rabbit_code:
        for func in funcs:
            check_rabbit(func)


def test_pass_at_k():   
    score1 = pass_at_k(scot_gpt, check_rabbit)
    score2 = pass_at_k(scot_gemini, check_rabbit)
    score3 = pass_at_k(sedit_gpt, check_rabbit)
    score4 = pass_at_k(sedit_gemini, check_rabbit)
    print(f"Pass@k score scot gpt: {score1}")
    print(f"Pass@k score scot gemini: {score2}")
    print(f"Pass@k score sedit gpt: {score3}")
    print(f"Pass@k score sedit gemini: {score4}")
    assert score1 >= 0.5
    assert score2 >= 0.5
    assert score3 >= 0.5
    assert score4 >= 0.5