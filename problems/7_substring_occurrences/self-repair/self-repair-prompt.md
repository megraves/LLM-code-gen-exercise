Give 5 different solutions for this problem labeled func1 through func5. Write a python program that follows the specification below. If there are mistakes in your answer, repair them.

def how_many_times(string: str, substring: str) -> int:
""" Find how many times a given substring can be found in the original string. Count overlaping cases.
>>> how_many_times('', 'a')
0
>>> how_many_times('aaa', 'a')
3
>>> how_many_times('aaaa', 'aa')
3
"""