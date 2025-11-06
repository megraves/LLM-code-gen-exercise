# import for testing pass@k metric
from .pass_at_k_metric import pass_at_k

# Import the generated functions to be tested
from ..problems.hard.firstgptcode import first_gpt
from ..problems.hard.firstgeminicode import first_gemini
from ..problems.hard.secondgptcode import second_gpt
from ..problems.hard.secondgeminicode import second_gemini

hard_code = [first_gpt, first_gemini, second_gpt, second_gemini]

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

def check_hard(func):
    try:
        assert func(rectangles) == expected_path
        assert func(same_rects) == same_expected
        return True
    except AssertionError:
        return False
    except Exception:
        return False

def test_hard():
    for funcs in hard_code:
        for func in funcs:
            check_hard(func)


def test_pass_at_k():   
    score1 = pass_at_k(first_gpt, check_hard)
    score2 = pass_at_k(first_gemini, check_hard)
    score3 = pass_at_k(second_gpt, check_hard)
    score4 = pass_at_k(second_gemini, check_hard)
    print(f"Pass@k score first gpt: {score1}")
    print(f"Pass@k score first gemini: {score2}")
    print(f"Pass@k score second gpt: {score3}")
    print(f"Pass@k score second gemini: {score4}")
    assert score1 >= 0.5
    assert score2 >= 0.5
    assert score3 >= 0.5
    assert score4 >= 0.5