# FROM HUMANEVAL: https://huggingface.co/datasets/openai/openai_humaneval/viewer/openai_humaneval/test?views%5B%5D=test&row=8

from solutions import funcs
from pass_at_k_metric import pass_at_k

rectangles = [
    {'x': 2, 'y': 2, 'width': 5, 'height': 4},
    {'x': 4, 'y': 3, 'width': 6, 'height': 6},
    {'x': 8, 'y': 1, 'width': 5, 'height': 4}
]

expected_path = [
    {'x': 2, 'y': 2},
    {'x': 7, 'y': 2},
    {'x': 7, 'y': 3},
    {'x': 8, 'y': 3},
    {'x': 8, 'y': 1},
    {'x': 13, 'y': 1},
    {'x': 13, 'y': 5},
    {'x': 10, 'y': 5},
    {'x': 10, 'y': 9},
    {'x': 4, 'y': 9},
    {'x': 4, 'y': 6},
    {'x': 2, 'y': 6},
]

same_rects = [
    {'x': 0, 'y': 0, 'width': 1, 'height': 1},
    {'x': 0, 'y': 0, 'width': 1, 'height': 1},    
    {'x': 0, 'y': 0, 'width': 1, 'height': 1}
]

same_expected = [
    {'x': 0, 'y': 0},
    {'x': 1, 'y': 0},
    {'x': 1, 'y': 1},
    {'x': 0, 'y': 1},
]

def check_outline(func):
    try:
        assert func(rectangles) == expected_path
        assert func(same_rects) == same_expected
        return True # Explicitly return True on success
    except AssertionError as e:
        print(f"Function {func.__name__} failed assertion: {e}")
        return False
    except Exception as e:
        print(f"Function {func.__name__} raised exception: {e}")
        return False

def test_funcs():
    for func in funcs:
        check_outline(func)

def test_pass_at_k():   
    score = pass_at_k(funcs, check_outline)
    print(f"The pass@k score is: {score}")
    assert score >= 0.5