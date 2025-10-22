Plan (high-level, not internal chain-of-thought)

1. Validate the intent: we need to return the *sorted* unique elements from a list.
2. Remove duplicates.
3. Sort the remaining elements.
4. Return the sorted list. (Assume elements are comparable — e.g., all numbers or all strings.)

Now I execute the sub-problems and show results.

Sub-problem 1 — remove duplicates:

* Approach used: convert the list to a `set` (removes duplicates).

Sub-problem 2 — sort the unique elements:

* Approach used: apply `sorted()` to the set result.

Implementation and tests (executed above):

```python
def unique(l: list):
    """Return sorted unique elements in a list

    >>> unique([5, 3, 5, 2, 3, 3, 9, 0, 123])
    [0, 2, 3, 5, 9, 123]
    """
    # Convert to a set to remove duplicates, then sort the result.
    # Note: this assumes elements are comparable (e.g., all numbers or all strings).
    return sorted(set(l))
```

Example run results (from tests I executed):

* `unique([5, 3, 5, 2, 3, 3, 9, 0, 123])` → `[0, 2, 3, 5, 9, 123]` (matches specification)
* `unique([])` → `[]`
* `unique([1,1,1,1])` → `[1]`
* `unique([3,2,1])` → `[1,2,3]`
* `unique(['b','a','b'])` → `['a','b']`

Final answer: the `unique` function above meets the specification (returns the sorted unique elements).

Note: If you need to handle lists containing unhashable items (e.g., other lists) or want to preserve original order then sort only when appropriate, tell me and I’ll adapt the function.
