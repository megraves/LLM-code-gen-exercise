# import for testing pass@k metric
from ..pass_at_k_metric import pass_at_k

# Import the generated functions to be tested
from ...problems.rescale.scotgptcode import scot_gpt
from ...problems.rescale.scotgeminicode import scot_gemini
from ...problems.rescale.seditgptcode import sedit_gpt
from ...problems.rescale.seditgeminicode import sedit_gemini

rescale_code = [scot_gpt, scot_gemini, sedit_gpt, sedit_gemini]

def check_rescale(func):
    try:
        # Original core cases
        assert func([2.0, 49.9]) == [0.0, 1.0]
        assert func([100.0, 49.9]) == [1.0, 0.0]
        assert func([1.0, 2.0, 3.0, 4.0, 5.0]) == [0.0, 0.25, 0.5, 0.75, 1.0]
        assert func([2.0, 1.0, 5.0, 3.0, 4.0]) == [0.25, 0.0, 1.0, 0.5, 0.75]
        assert func([12.0, 11.0, 15.0, 13.0, 14.0]) == [0.25, 0.0, 1.0, 0.5, 0.75]

        # ✅ Additional edge cases

        # 1. All elements equal (edge for division by zero)
        assert func([5.0, 5.0, 5.0]) == [0.0, 0.0, 0.0]

        # 2. Negative numbers
        assert func([-5.0, 0.0, 5.0]) == [0.0, 0.5, 1.0]

        # 3. Fractional numbers
        assert func([0.1, 0.2, 0.4, 0.8]) == [0.0, 0.14285714285714285, 0.42857142857142855, 1.0]

        # 4. Already in range [0,1]
        assert func([0.0, 0.25, 0.5, 0.75, 1.0]) == [0.0, 0.25, 0.5, 0.75, 1.0]

        # 5. Duplicates and unsorted
        assert func([3.0, 3.0, 1.0, 2.0, 2.0]) == [1.0, 1.0, 0.0, 0.5, 0.5]

        # 6. Very large/small values
        assert func([1e9, 1e9 + 1]) == [0.0, 1.0]
        assert func([-1e-9, 1e-9]) == [0.0, 1.0]

        return True
    except AssertionError as e:
        print(f"Assertion failed for {func.__name__} with error {e}")
        raise e


def test_rescale():
    for funcs in rescale_code:
        for func in funcs:
            check_rescale(func)

def test_pass_at_k():   
    score1 = pass_at_k(scot_gpt, check_rescale)
    score2 = pass_at_k(scot_gemini, check_rescale)
    score3 = pass_at_k(sedit_gpt, check_rescale)
    score4 = pass_at_k(sedit_gemini, check_rescale)
    print(f"Pass@k score scot gpt: {score1}")
    print(f"Pass@k score scot gemini: {score2}")
    print(f"Pass@k score sedit gpt: {score3}")
    print(f"Pass@k score sedit gemini: {score4}")
    assert score1 >= 0.5
    assert score2 >= 0.5
    assert score3 >= 0.5
    assert score4 >= 0.5