from solutions import funcs
from pass_at_k_metric import pass_at_k

def check_rescale(func):
    try:
        assert func([2.0, 49.9]) == [0.0, 1.0]
        assert func([100.0, 49.9]) == [1.0, 0.0]
        assert func([1.0, 2.0, 3.0, 4.0, 5.0]) == [0.0, 0.25, 0.5, 0.75, 1.0]
        assert func([2.0, 1.0, 5.0, 3.0, 4.0]) == [0.25, 0.0, 1.0, 0.5, 0.75]
        assert func([12.0, 11.0, 15.0, 13.0, 14.0]) == [0.25, 0.0, 1.0, 0.5, 0.75]
    except AssertionError:
        return False

def test_funcs():
    for func in funcs:
        check_rescale(func)

def test_pass_at_k():   
    score = pass_at_k(funcs, check_rescale)
    assert score >= 0.5