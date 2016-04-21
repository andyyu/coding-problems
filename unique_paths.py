# Andy Yu
'''
A robot is located at the top-left corner of a m x n grid (marked 'R' in the diagram below).

The robot can only move either down or right at any point in time. 
The robot is trying to reach the bottom-right corner of the grid (marked 'F' in the diagram below).

How many possible unique paths are there?

[R] [ ] [ ] [ ] [ ] [ ] [ ]
[ ] [ ] [ ] [ ] [ ] [ ] [ ]
[ ] [ ] [ ] [ ] [ ] [ ] [F]

(Above is a 3 x 7 grid. How many possible unique paths are there?)

Note: m and n will be at most 100.

Difficulty: Medium

Solution notes:
My initial thought is that for any given m x n matrix, the robot must move down m-1 times, and move right n-1 times.
Then, the number of unique paths is the number of unique ways you can put m-1 "down" moves and n-1 "right" moves in
m-1+n-1 total moves. This is simple combinatorics, and so can be found by C(m+n-2, m-1) - choose m-1 "down" moves
out of m+n-2 total moves. The equation for this is (m+n-2)! / (m-1)!(n-1)!

def unique_paths(m, n):
        return math.factorial(m+n-2)/(math.factorial(m-1)*math.factorial(n-1))

O(1) time
O(1) space

Another way to do this is with dynamic programming. This solution is written below and involves iterating over all
squares in the grid and updating the "number" of paths one can take to get to each square by adding the number of
unique paths you can take to get to the square above and to the left of it (the only squares the robot can come from).

O(m*n) time
O(m*n) space
'''

def uniquePaths(m, n):
  grid = [[1 for i in xrange(n)] for j in xrange(m)]
  for i in xrange(1, n):
    for j in xrange(1, m):
      grid[i][j] = grid[i-1][j] + grid[i][j-1]
  return grid[m-1][n-1]


