# import for testing pass@k metric
from .pass_at_k_metric import pass_at_k

# Import the generated functions to be tested
from ..problems.sort.cotgptcode import cot_gpt
from ..problems.sort.cotgeminicode import cot_gemini
from ..problems.sort.splangptcode import splan_gpt
from ..problems.sort.splangeminicode import splan_gemini

sort_code = [cot_gpt, cot_gemini, splan_gpt, splan_gemini]

def check_sort(func):
    try:
        # Test Case 1 (Original)
        input_1 = [5, 3, 5, 2, 3, 3, 9, 0, 123]
        expected_1 = [0, 2, 3, 5, 9, 123]
        assert func(input_1) == expected_1
        
        # Test Case 2 (Empty List)
        input_2 = []
        expected_2 = []
        assert func(input_2) == expected_2
        
        # Test Case 3 (All unique and sorted)
        input_3 = [1, 2, 3, 4]
        expected_3 = [1, 2, 3, 4]
        assert func(input_3) == expected_3
        
        # Test Case 4 (Duplicates, unsorted, negative numbers)
        input_4 = [10, -5, 10, 0, -5, 7]
        expected_4 = [-5, 0, 7, 10]
        assert func(input_4) == expected_4
        
        # If all assertions pass
        print(f"Function {func.__name__} PASSED all tests.")
        return True
    except AssertionError:
        return False
    except Exception:
        return False

def test_sort():
    for funcs in sort_code:
        for func in funcs:
            check_sort(func)


def test_pass_at_k():   
    score1 = pass_at_k(cot_gpt, check_sort)
    score2 = pass_at_k(cot_gemini, check_sort)
    score3 = pass_at_k(splan_gpt, check_sort)
    score4 = pass_at_k(splan_gemini, check_sort)
    print(f"Pass@k score cot gpt: {score1}")
    print(f"Pass@k score cot gemini: {score2}")
    print(f"Pass@k score splan gpt: {score3}")
    print(f"Pass@k score splan gemini: {score4}")
    assert score1 >= 0.5
    assert score2 >= 0.5
    assert score3 >= 0.5
    assert score4 >= 0.5