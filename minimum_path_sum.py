# Andy Yu
'''
There is a m x n grid filled with non-negative numbers.
Find a path from top left to bottom right which minimizes the sum of all numbers along its path.

You can only move down or right.

Difficulty: Medium

Solution notes:

Since we can only move down or right, a number can only be landed on from the number above it, or to the left of it.
We can use this idea to update the minimum path up to all the indices in the grid in-place.
We start by establishing the minimum path for the first row and column.
This is easy because all of the square in the first row / first column can only be reached by one other square.
Then, we can go through the rest of the squares and update each square's minimum path by just adding it's own number + the lesser of the minimum path of the square above or to the left of it.
The only caveat is we must go through in order such that for every square we encounter, we must have already updated the minimum path of the square above/left of it.
Then once we update the last square of the grid, we only have to return its updated number as the minimum path.

O(MN) time
O(1) space

'''
def min_path_sum(grid):
  for i in range(1, len(grid[0])):
      grid[0][i] += grid[0][i-1]
  for i in range(1, len(grid)):
      grid[i][0] += grid[i-1][0]
  for i in range(1, len(grid)):
      for j in range(1, len(grid[0])):
          grid[i][j] += min(grid[i-1][j], grid[i][j-1])
  return grid[-1][-1]