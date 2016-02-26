# Andy Yu
'''
Given a 2d array of 1s and 0s, find the size of the largest square of 1s in the matrix.
Difficulty: Medium - Hard

Solution: 
O(n) time
O(1) space
dynamic programming
This solution works by iterating through all cells from the top left to the bottom right. We calculate the largest
square that can be created from each cell if it were the bottom right hand corner of a square, doing so by incrementing
the value of that cell with the smallest value of the (cell to the left, above, and upper left).
i.e.
0 0 0       0 0 0
0 1 1   =>  0 1 1
0 1 1       0 1 2

'''
# Example: this should return 3
num_list = [[0, 1, 1, 1, 1, 1, 1, 0], 
            [0, 1, 1, 1, 1, 1, 1, 0],
            [0, 1, 1, 1, 0, 1, 0, 1],
            [0, 1, 1, 1, 1, 1, 0, 1],
            [0, 0, 0, 0, 0, 0, 0, 0]]

max_cell_count = 0
for row in xrange(len(num_list)):
  for col in xrange(len(num_list[row])):
    if num_list[row][col] == 1:
      top_cell = num_list[row-1][col]
      left_cell = num_list[row][col-1]
      tl_cell = num_list[row-1][col-1]
      if top_cell > 0 and left_cell > 0 and tl_cell > 0:
        num_list[row][col] += min([top_cell, left_cell, tl_cell])
      if num_list[row][col] > max_cell_count:
        max_cell_count = num_list[row][col]

print max_cell_count



