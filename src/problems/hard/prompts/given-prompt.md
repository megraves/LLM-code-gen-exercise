<!-- From the article: https://peter-kullmann.medium.com/all-major-llms-struggle-with-this-simple-programming-task-3e6903fae3a2 -->

Give 5 different solutions for this problem labeled func1 through func5. Create a python function that takes list of overlapping rectangles (given with the coordinate of the top left corner and width and height) and calculates the rectangular polygonal path that tightly outlines the rectangles. The result should be an array of points. The origin of the coordinate system is top left.

As an example, for following rectangles:
[
{ x: 2, y: 2, width: 5, height: 4 },
{ x: 4, y: 3, width: 6, height: 6 },
{ x: 8, y: 1, width: 5, height: 4 }
]
the function should return following path:
[
{ x: 2, y: 2 },
{ x: 7, y:2 },
{ x: 7, y: 3 },
{ x: 8, y: 3 },
{ x: 8, y: 1 },
{ x: 13, y: 1 },
{ x: 13, y: 5 },
{ x: 10, y: 5 },
{ x: 10, y: 9 },
{ x: 4, y: 9 },
{ x: 4, y: 6 },
{ x: 2, y: 6 },
]