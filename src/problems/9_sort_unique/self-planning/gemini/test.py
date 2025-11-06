# FROM HUMANEVAL: https://huggingface.co/datasets/openai/openai_humaneval/viewer/openai_humaneval/test?views%5B%5D=test&row=8

from solutions import funcs
from pass_at_k_metric import pass_at_k

def check_unique(func):
    """
    Tests if the function correctly returns a sorted list of unique elements.
    """
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
        # Catch assertion errors (incorrect output)
        print(f"Function {func.__name__} FAILED an assertion test.")
        # Optional: Log the specific failure for better debugging
        # print(f"Input was {input_4}, received {func(input_4)}, expected {expected_4}")
        return False
    
    except Exception as e:
        # Catch other exceptions (like TypeError, RecursionError)
        print(f"Function {func.__name__} failed with an unhandled exception: {e}")
        return False

def test_funcs():
    for func in funcs:
        check_unique(func)

def test_pass_at_k():   
    score = pass_at_k(funcs, check_unique)
    print(f"Pass@k score: {score}")
    assert score >= 0.5