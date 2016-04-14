# Andy Yu
'''
Given a triangle, find the minimum path sum from top to bottom. 
Each step you may move to adjacent numbers on the row below.

For example, given the following triangle
[
     [2],
    [3,4],
   [6,5,7],
  [4,1,8,3]
]
The minimum path sum from top to bottom is 11 (i.e., 2 + 3 + 5 + 1 = 11).

Note:
Bonus point if you are able to do this using only O(n) extra space, 
where n is the total number of rows in the triangle.

Difficulty: Medium

Solution notes:
O(n) time
O(1) space

update triangle in place, top-down
'''

def minimum_path(triangle):
  for i in xrange(1, len(triangle)):
    triangle[i][0] += triangle[i-1][0]  # first element of row
    triangle[i][i] += triangle[i-1][i-1]  # last element of row
    for j in xrange(1, i):
      smallest_prev = min(triangle[i-1][j-1], triangle[i-1][j]) # smallest above path
      triangle[i][j] += smallest_prev
  return min(triangle[len(triangle)-1])

