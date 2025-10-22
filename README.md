# LLM-code-gen-exercise
for Theory and Practice of Software Engineering CS520 UMass

Deliverables:
Submit one PDF document on Gradescope. The PDF should include:
  - Prompts, methodology, experiments, results (with pass@k), debugging analysis, and innovation discussion.
  - A link to your GitHub repository, which must contain:
    - Prompts and/or workflows/scripts used
    - Generated code
    - Test cases (dataset-provided or self-written)
    - Evaluation scripts and results

## Part 0 - Choose at least 2 LLMs from different families
- GPT-4
- LLaMa-2
- Gemini


## Part 1 - Prompt Design and Code Generation
### 1a - Select 10 Programming Problems
These programming problems were selected from the HumanEval dataset and LeetCode.

1. Hungry Rabbit [(HumanEval/159)](https://huggingface.co/datasets/openai/openai_humaneval/viewer/openai_humaneval/test?p=1&views%5B%5D=test&row=159)
    ```
    def eat(number, need, remaining):
    """
    You're a hungry rabbit, and you already have eaten a certain number of carrots,
    but now you need to eat more carrots to complete the day's meals.
    you should return an array of [ total number of eaten carrots after your meals,
    the number of carrots left after your meals ]
    if there are not enough remaining carrots, you will eat all remaining carrots, but will still be hungry.

    Example:
    * eat(5, 6, 10) -> [11, 4]
    * eat(4, 8, 9) -> [12, 1]
    * eat(1, 10, 10) -> [11, 0]
    * eat(2, 11, 5) -> [7, 0]

    Variables:
    @number : integer
    the number of carrots that you have eaten.
    @need : integer
    the number of carrots that you need to eat.
    @remaining : integer
    the number of remaining carrots thet exist in stock

    Constrain:
    * 0 <= number <= 1000
    * 0 <= need <= 1000
    * 0 <= remaining <= 1000

    Have fun :)
    """
    ```

2. Make a Pile [(HumanEval/100)](https://huggingface.co/datasets/openai/openai_humaneval/viewer/openai_humaneval/test?p=1&views%5B%5D=test&row=100)
    ```
    def make_a_pile(n):
    """
    Given a positive integer n, you have to make a pile of n levels of stones.
    The first level has n stones.
    The number of stones in the next level is:
    - the next odd number if n is odd.
    - the next even number if n is even.
    Return the number of stones in each level in a list, where element at index
    i represents the number of stones in the level (i+1).

    Examples:
    >>> make_a_pile(3)
    [3, 5, 7]
    """
    ```

3. Words String [(HumanEval/101)](https://huggingface.co/datasets/openai/openai_humaneval/viewer/openai_humaneval/test?p=1&views%5B%5D=test&row=101)
    ```
    def words_string(s):
    """
    You will be given a string of words separated by commas or spaces. Your task is
    to split the string into words and return an array of the words.

    For example:
    words_string("Hi, my name is John") == ["Hi", "my", "name", "is", "John"]
    words_string("One, two, three, four, five, six") == ["One", "two", "three", "four", "five", "six"]
    """
    ```

4. Odd in Even [(HumanEval/121)](https://huggingface.co/datasets/openai/openai_humaneval/viewer/openai_humaneval/test?p=1&views%5B%5D=test&row=121)
    ```
    def solution(lst):
    """Given a non-empty list of integers, return the sum of all of the odd elements that are in even positions.

    Examples
    solution([5, 8, 7, 1]) ==> 12
    solution([3, 3, 3, 3, 3]) ==> 9
    solution([30, 13, 24, 321]) ==>0
    """
    ```

5. Unit Rescale [(HumanEval/21)](https://huggingface.co/datasets/openai/openai_humaneval/viewer/openai_humaneval/test?row=21)
    ```
    from typing import List

    def rescale_to_unit(numbers: List[float]) -> List[float]:
    """ Given list of numbers (of at least two elements), apply a linear transform to that list,
    such that the smallest number will become 0 and the largest will become 1
    >>> rescale_to_unit([1.0, 2.0, 3.0, 4.0, 5.0])
    [0.0, 0.25, 0.5, 0.75, 1.0]
    """
    ```

6. Sum Product [(HumanEval1/8)](https://huggingface.co/datasets/openai/openai_humaneval/viewer/openai_humaneval/test?views%5B%5D=test&row=8)
    ```
    from typing import List, Tuple

    def sum_product(numbers: List[int]) -> Tuple[int, int]:
    """ For a given list of integers, return a tuple consisting of a sum and a product of all the integers in a list.
    Empty sum should be equal to 0 and empty product should be equal to 1.
    >>> sum_product([])
    (0, 1)
    >>> sum_product([1, 2, 3, 4])
    (10, 24)
    """
    ```

7. How Many Times Substring [(HumanEval1/18)](https://huggingface.co/datasets/openai/openai_humaneval/viewer/openai_humaneval/test?views%5B%5D=test&row=18)
    ```
    def how_many_times(string: str, substring: str) -> int:
    """ Find how many times a given substring can be found in the original string. Count overlaping cases.
    >>> how_many_times('', 'a')
    0
    >>> how_many_times('aaa', 'a')
    3
    >>> how_many_times('aaaa', 'aa')
    3
    """
    ```

8. Flip Case [(HumanEval1/27)](https://huggingface.co/datasets/openai/openai_humaneval/viewer/openai_humaneval/test?views%5B%5D=test&row=27)
    ```
    def flip_case(string: str) -> str:
    """ For a given string, flip lowercase characters to uppercase and uppercase to lowercase.
    >>> flip_case('Hello')
    'hELLO'
    """
    ```

9. Sorted Unique Elements [(HumanEval1/34)](https://huggingface.co/datasets/openai/openai_humaneval/viewer/openai_humaneval/test?views%5B%5D=test&row=34)
    ```
    def unique(l: list):
    """Return sorted unique elements in a list
    >>> unique([5, 3, 5, 2, 3, 3, 9, 0, 123])
    [0, 2, 3, 5, 9, 123]
    """
    ```

10. Largest Prime Factor [(HumanEval1/59)](https://huggingface.co/datasets/openai/openai_humaneval/viewer/openai_humaneval/test?views%5B%5D=test&row=59)
    ```
    def largest_prime_factor(n: int):
    """Return the largest prime factor of n. Assume n > 1 and is not a prime.
    >>> largest_prime_factor(13195)
    29
    >>> largest_prime_factor(2048)
    2
    """
    ```


### 1b - Prompts, Code Generation, and Results

Each file in the `problems` directory has the prompts and generated files across two different LLMs:

```
problems
    |
    ---+ problem_name
        |
        ---+ prompting_strat_1
        |       |
        |       ---+ LLM_1
        |       |   |
        |       |   ---+ solutions.md       # shows the generated solution from the 
        |       |   ---+ solutions.py       # shows the generated code (k=five different functions)
        |       |   ---+ test.py            # implements the test from HumanEval on all five functions (run with pytest)
        |       ---+ LLM_2  
        |       ---+ strat-prompt.md        # shows the prompt given to the LLMs based on the given strategy
        ---+ prompting_strat_2
```  

The results are as follows using the pass@k metric.

| #1          | Gemini | GPT    |
|-------------|--------|--------|
| Prompting   | pass@k | pass@k |
| scot        | 1.0    | 1.0    |
| self-edit   | 1.0    | 1.0    |

| #2          | Gemini | GPT    |
|-------------|--------|--------|
| Prompting   | pass@k | pass@k |
| cot         | 1.0    | 1.0    |
| self-debug  | 1.0    | 1.0    |

| #3          | Gemini | GPT    |
|-------------|--------|--------|
| Prompting   | pass@k | pass@k |
| scot        | 1.0    | 1.0    |
| self-plan   | 1.0    | 1.0    |

| #4          | Gemini | GPT    |
|-------------|--------|--------|
| Prompting   | pass@k | pass@k |
| cot         | 1.0    | 1.0    |
| self-debug  | 1.0    | 1.0    |

| #5          | Gemini | GPT    |
|-------------|--------|--------|
| Prompting   | pass@k | pass@k |
| scot        | 1.0    | 1.0    |
| self-edit   | 1.0    | 1.0    |

| #6          | Gemini | GPT    |
|-------------|--------|--------|
| Prompting   | pass@k | pass@k |
| cot         | 1.0    | 1.0    |
| self-edit   | 1.0    | 1.0*   |
*The gpt had an import error related to by local environment `import numpy as np`. When running `pip install numpy`, all funcs ran and passed. 

| #7          | Gemini | GPT    |
|-------------|--------|--------|
| Prompting   | pass@k | pass@k |
| scot        | 1.0    | 1.0    |
| self-repair | 1.0    | 1.0    |

| #8          | Gemini | GPT    |
|-------------|--------|--------|
| Prompting   | pass@k | pass@k |
| scot        | 1.0*   | 1.0    |
| self-plan   | 1.0    | 1.0    |
*The gemini had an import error when using `from typing import str`. When commented out, all funcs ran and passed.

| #9          | Gemini | GPT    |
|-------------|--------|--------|
| Prompting   | pass@k | pass@k |
| self-plan   | 1.0    | 1.0    |
| cot         | 1.0    | 1.0    |

| #10         | Gemini | GPT    |
|-------------|--------|--------|
| Prompting   | pass@k | pass@k |
| self-repair | 1.0    | 1.0    |
| cot         | 1.0    | 1.0    |
