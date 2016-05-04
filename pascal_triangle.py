# Andy Yu
'''
Given numRows, generate the first numRows of Pascal's triangle.

For example, given numRows = 5,
Return

[
     [1],
    [1,1],
   [1,2,1],
  [1,3,3,1],
 [1,4,6,4,1]
]

Difficulty: Easy - Medium

Solution notes:
O(n^2) time
O(1) space

'''
def generate_pascal(numRows):
  triangle = []
  for i in xrange(0, numRows):
      new_row = [1] * (i+1)
      for j in xrange(1, i):
          new_row[j] = triangle[i-1][j-1] + triangle[i-1][j]
      triangle.append(new_row)
  return triangle

