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

1. Permutations [(LeetCode)](https://leetcode.com/problems/permutations/description/)
    ```
    Given an array nums of distinct integers, return all the possible permutations. You can return the answer in any order.

    Example 1:

    Input: nums = [1,2,3]
    Output: [[1,2,3],[1,3,2],[2,1,3],[2,3,1],[3,1,2],[3,2,1]]
    Example 2:

    Input: nums = [0,1]
    Output: [[0,1],[1,0]]
    Example 3:

    Input: nums = [1]
    Output: [[1]]
    

    Constraints:

    1 <= nums.length <= 6
    -10 <= nums[i] <= 10
    All the integers of nums are unique.
    ```

2. Palindrome Number [(LeetCode)](https://leetcode.com/problems/palindrome-number/description/)
    ```
    Given an integer x, return true if x is a palindrome, and false otherwise. 

    Example 1:

    Input: x = 121
    Output: true
    Explanation: 121 reads as 121 from left to right and from right to left.
    Example 2:

    Input: x = -121
    Output: false
    Explanation: From left to right, it reads -121. From right to left, it becomes 121-. Therefore it is not a palindrome.
    Example 3:

    Input: x = 10
    Output: false
    Explanation: Reads 01 from right to left. Therefore it is not a palindrome.
    

    Constraints:

    -231 <= x <= 231 - 1
    

    Follow up: Could you solve it without converting the integer to a string?
    ```

3. Two Sum [(LeetCode)](https://leetcode.com/problems/two-sum/description/)
    ```
    Given an array of integers nums and an integer target, return indices of the two numbers such that they add up to target.

    You may assume that each input would have exactly one solution, and you may not use the same element twice.

    You can return the answer in any order.

    Example 1:

    Input: nums = [2,7,11,15], target = 9
    Output: [0,1]
    Explanation: Because nums[0] + nums[1] == 9, we return [0, 1].
    Example 2:

    Input: nums = [3,2,4], target = 6
    Output: [1,2]
    Example 3:

    Input: nums = [3,3], target = 6
    Output: [0,1]
    

    Constraints:

    2 <= nums.length <= 104
    -109 <= nums[i] <= 109
    -109 <= target <= 109
    Only one valid answer exists.
    

    Follow-up: Can you come up with an algorithm that is less than O(n2) time complexity?
    ```

4. Add Binary [(LeetCode)](https://leetcode.com/problems/add-binary/description/)
    ```
    Given two binary strings a and b, return their sum as a binary string.

    Example 1:

    Input: a = "11", b = "1"
    Output: "100"
    Example 2:

    Input: a = "1010", b = "1011"
    Output: "10101"
    

    Constraints:

    1 <= a.length, b.length <= 104
    a and b consist only of '0' or '1' characters.
    Each string does not contain leading zeros except for the zero itself.
    ```

5. Valid Parenthesis [(LeetCode)](https://leetcode.com/problems/valid-parentheses/description/)
    ```
    Given a string s containing just the characters '(', ')', '{', '}', '[' and ']', determine if the input string is valid.

    An input string is valid if:

    Open brackets must be closed by the same type of brackets.
    Open brackets must be closed in the correct order.
    Every close bracket has a corresponding open bracket of the same type.

    Example 1:

    Input: s = "()"

    Output: true

    Example 2:

    Input: s = "()[]{}"

    Output: true

    Example 3:

    Input: s = "(]"

    Output: false

    Example 4:

    Input: s = "([])"

    Output: true

    Example 5:

    Input: s = "([)]"

    Output: false

    Constraints:

    1 <= s.length <= 104
    s consists of parentheses only '()[]{}'.
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

1. Permutations

    Gemini
    |    | Prompting Strategy | Prompt | Tests | Solution | pass@k | Explanation |
    |----|--------------------|--------|-------|----------|--------|-------------|
    | 1. |                    |        |       |          |        |             |
    | 2. |                    |        |       |          |        |             |

    GPT-4
    |    | Prompting Strategy | Prompt | Tests | Solution | pass@k | Explanation |
    |----|--------------------|--------|-------|----------|--------|-------------|
    | 1. |                    |        |       |          |        |             |
    | 2. |                    |        |       |          |        |             |


2. Palindrome Number

    Gemini
    |    | Prompting Strategy | Prompt | Tests | Solution | pass@k | Explanation |
    |----|--------------------|--------|-------|----------|--------|-------------|
    | 1. |                    |        |       |          |        |             |
    | 2. |                    |        |       |          |        |             |

    GPT-4
    |    | Prompting Strategy | Prompt | Tests | Solution | pass@k | Explanation |
    |----|--------------------|--------|-------|----------|--------|-------------|
    | 1. |                    |        |       |          |        |             |
    | 2. |                    |        |       |          |        |             |


3. Two Sum

    Gemini
    |    | Prompting Strategy | Prompt | Tests | Solution | pass@k | Explanation |
    |----|--------------------|--------|-------|----------|--------|-------------|
    | 1. |                    |        |       |          |        |             |
    | 2. |                    |        |       |          |        |             |

    GPT-4
    |    | Prompting Strategy | Prompt | Tests | Solution | pass@k | Explanation |
    |----|--------------------|--------|-------|----------|--------|-------------|
    | 1. |                    |        |       |          |        |             |
    | 2. |                    |        |       |          |        |             |


4. Add Binary

    Gemini
    |    | Prompting Strategy | Prompt | Tests | Solution | pass@k | Explanation |
    |----|--------------------|--------|-------|----------|--------|-------------|
    | 1. |                    |        |       |          |        |             |
    | 2. |                    |        |       |          |        |             |

    GPT-4
    |    | Prompting Strategy | Prompt | Tests | Solution | pass@k | Explanation |
    |----|--------------------|--------|-------|----------|--------|-------------|
    | 1. |                    |        |       |          |        |             |
    | 2. |                    |        |       |          |        |             |


5. Valid Parenthesis

    Gemini
    |    |Prompt Strat |    Prompt        | Tests | Solution | pass@k | Explanation |
    |----|--------------------|------------------|-------|----------|--------|-------------|
    | 1. | C-o-T  |[img](./6-prompt.png)|       |          |     |          |
    | 2. |                    |                |       |          |        |             |

    GPT-4
    |    | Prompting Strategy | Prompt | Tests | Solution | pass@k | Explanation |
    |----|--------------------|--------|-------|----------|--------|-------------|
    | 1. |                    |        |       |          |        |             |
    | 2. |                    |        |       |          |        |             |


6. Sum Product

    Gemini
    |    | Prompting Strategy | Prompt | Tests | Solution | pass@k | Explanation |
    |----|--------------------|--------|-------|----------|--------|-------------|
    | 1. |                    |        |       |          |        |             |
    | 2. |                    |        |       |          |        |             |

    GPT-4
    |    | Prompting Strategy | Prompt | Tests | Solution | pass@k | Explanation |
    |----|--------------------|--------|-------|----------|--------|-------------|
    | 1. |                    |        |       |          |        |             |
    | 2. |                    |        |       |          |        |             |


7. How Many Times Substring

    Gemini
    |    | Prompting Strategy | Prompt | Tests | Solution | pass@k | Explanation |
    |----|--------------------|--------|-------|----------|--------|-------------|
    | 1. |                    |        |       |          |        |             |
    | 2. |                    |        |       |          |        |             |

    GPT-4
    |    | Prompting Strategy | Prompt | Tests | Solution | pass@k | Explanation |
    |----|--------------------|--------|-------|----------|--------|-------------|
    | 1. |                    |        |       |          |        |             |
    | 2. |                    |        |       |          |        |             |


8. Flip Case

    Gemini
    |    | Prompting Strategy | Prompt | Tests | Solution | pass@k | Explanation |
    |----|--------------------|--------|-------|----------|--------|-------------|
    | 1. |                    |        |       |          |        |             |
    | 2. |                    |        |       |          |        |             |

    GPT-4
    |    | Prompting Strategy | Prompt | Tests | Solution | pass@k | Explanation |
    |----|--------------------|--------|-------|----------|--------|-------------|
    | 1. |                    |        |       |          |        |             |
    | 2. |                    |        |       |          |        |             |


9.  Sorted Unique Elements

    Gemini
    |    | Prompting Strategy | Prompt | Tests | Solution | pass@k | Explanation |
    |----|--------------------|--------|-------|----------|--------|-------------|
    | 1. |                    |        |       |          |        |             |
    | 2. |                    |        |       |          |        |             |

    GPT-4
    |    | Prompting Strategy | Prompt | Tests | Solution | pass@k | Explanation |
    |----|--------------------|--------|-------|----------|--------|-------------|
    | 1. |                    |        |       |          |        |             |
    | 2. |                    |        |       |          |        |             |


10. Largest Prime Factor

    Gemini
    |    | Prompting Strategy | Prompt | Tests | Solution | pass@k | Explanation |
    |----|--------------------|--------|-------|----------|--------|-------------|
    | 1. |                    |        |       |          |        |             |
    | 2. |                    |        |       |          |        |             |

    GPT-4
    |    | Prompting Strategy | Prompt | Tests | Solution | pass@k | Explanation |
    |----|--------------------|--------|-------|----------|--------|-------------|
    | 1. |                    |        |       |          |        |             |
    | 2. |                    |        |       |          |        |             |

    

## Part 2 - Failure Problems
