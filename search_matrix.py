# Andy Yu
'''
Write an efficient algorithm that searches for a value in an m x n matrix. This matrix has the following properties:

Integers in each row are sorted from left to right.
The first integer of each row is greater than the last integer of the previous row.
For example,

Consider the following matrix:

[
  [1,   3,  5,  7],
  [10, 11, 16, 20],
  [23, 30, 34, 50]
]
Given target = 3, return true.

Difficulty: Medium

Solution notes:
O(M+N) time
O(1) space
'''

def search_matrix(matrix, target):
  target_row = len(matrix)-1
  for i in xrange(len(matrix)):
      if matrix[i][0] > target and i > 0:
          target_row = i-1
          break
  for num in matrix[target_row]:
      if num == target:
          return True
  return False


