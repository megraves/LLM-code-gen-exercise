# from HumanEval: https://huggingface.co/datasets/openai/openai_humaneval/viewer/openai_humaneval/test?views%5B%5D=test&row=27

from flip_case import flip_case, flip_case_manual

def test_flip_case():
    assert flip_case('') == ''
    assert flip_case('Hello!') == 'hELLO!'
    assert flip_case('These violent delights have violent ends') == 'tHESE VIOLENT DELIGHTS HAVE VIOLENT ENDS'

def test_flip_case_manual():
    assert flip_case_manual('') == ''
    assert flip_case_manual('Hello!') == 'hELLO!'
    assert flip_case_manual('These violent delights have violent ends') == 'tHESE VIOLENT DELIGHTS HAVE VIOLENT ENDS'