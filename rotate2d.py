# Andy Yu
'''
You are given an n x n 2D matrix representing an image.

Rotate the image by 90 degrees (clockwise).

1 0 1 0 0    0 0 1 0 1
0 0 0 1 0    1 1 1 0 0
1 1 1 1 1 => 1 0 1 0 1
0 1 0 0 1    0 0 1 1 0
0 1 1 0 0    0 1 1 0 0

Naive solution:
create a new n x n matrix and update values by traversing in the correct order.

Can we do this in place?

The approach is to iterate over the upper left hand corner of the array and "swap" 4 elements at a time.

Difficulty: Medium

Solution notes:
O(n) time // where n is the number of elements in the 2d array.
O(1) space

bonus: super pythonic version (not mine!)
def rotate(self, A):
  A[:] = zip(*A[::-1])

[::-1] reverses the order of the lists in the 2d array, so it essentially flips it upside down.
zip() "groups" the first element of each list into a list, the 2nd element of each list into the 2nd...
and so on. This results in transposition of the array.

'''

def rotate(matrix):
  n = len(matrix)
  for i in xrange(n/2):
    for j in xrange(n-n/2):
      matrix[i][j], matrix[n-1-j][i], matrix[n-1-i][n-1-j], matrix[j][n-1-i] = \
      matrix[n-1-j][i], matrix[n-1-i][n-1-j], matrix[j][n-1-i], matrix[i][j]
  return matrix
