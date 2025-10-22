Give 5 different solutions for this problem labeled func1 through func5. When creating solutions, you like to edit your work as you go. Show your work and the edits you make along the way. Given the programming specification below, create a solution.

from typing import List

def rescale_to_unit(numbers: List[float]) -> List[float]:
""" Given list of numbers (of at least two elements), apply a linear transform to that list,
such that the smallest number will become 0 and the largest will become 1
>>> rescale_to_unit([1.0, 2.0, 3.0, 4.0, 5.0])
[0.0, 0.25, 0.5, 0.75, 1.0]
"""

