# Andy Yu
'''
Given a m x n grid filled with non-negative numbers, 
find a path from top left to bottom right which minimizes the sum of all numbers along its path.

Difficulty: Medium

Solution notes:
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