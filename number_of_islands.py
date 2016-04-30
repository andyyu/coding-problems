# Andy Yu
'''

Given a 2d grid map of '1's (land) and '0's (water), count the number of islands. An island is surrounded by water and is formed by connecting adjacent lands horizontally or vertically. You may assume all four edges of the grid are all surrounded by water.

Example 1:

11110
11010
11000
00000
Answer: 1

Example 2:

11000
11000
00100
00011
Answer: 3

Difficulty: Medium

Solution notes:

Every time we encounter a "1", we know that it must be part of an island, so we increment the island counter by 1.
However, we don't want to count the "1"s attached to that one (part of the same island), so we must "sink" the island that
the counted "1" belongs to. To do this, I use a BFS approach with a stack, where adjacent "1"s are continuously added
to the stack and then set to 0.

'''

def num_islands(grid):
  num_islands = 0
  for i in xrange(len(grid)):
      for j in xrange(len(grid[i])):
          if grid[i][j] == "1":
              num_islands += 1
              self.sink_island(grid, i, j)
  return num_islands
                
def sink_island(grid, i, j):
  stack = [(i, j)]
  while stack:
      square = stack.pop()
      i = square[0]
      j = square[1]
      grid[i][j] = 0
      if i > 0 and grid[i-1][j] == "1":
          stack.append((i-1, j))
      if j > 0 and grid[i][j-1] == "1":
          stack.append((i, j-1))
      if i < len(grid) - 1 and grid[i+1][j] == "1":
          stack.append((i+1, j))
      if j < len(grid[i]) - 1 and grid[i][j+1] == "1":
          stack.append((i, j+1))