# From humaneval: https://huggingface.co/datasets/openai/openai_humaneval/viewer/openai_humaneval/test?views%5B%5D=test&row=18
from substr_occ import how_many_times

def test_substring_occurrences():
    assert how_many_times('', 'x') == 0
    assert how_many_times('xyxyxyx', 'x') == 4
    assert how_many_times('cacacacac', 'cac') == 4
    assert how_many_times('john doe', 'john') == 1
    # Add my own test out of curiosity
    assert how_many_times('xxxx', 'xx') == 3