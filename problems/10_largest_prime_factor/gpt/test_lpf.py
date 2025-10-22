# From HumanEval: https://huggingface.co/datasets/openai/openai_humaneval/viewer/openai_humaneval/test?views%5B%5D=test&row=59

from lpf import largest_prime_factor

def test_lpf():
    assert largest_prime_factor(15) == 5
    assert largest_prime_factor(27) == 3
    assert largest_prime_factor(63) == 7
    assert largest_prime_factor(330) == 11
    assert largest_prime_factor(13195) == 29