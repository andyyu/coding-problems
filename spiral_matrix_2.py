# Andy Yu
'''
Given an integer n, generate a square matrix filled with elements from 1 to n^2 in spiral order.

For example,
Given n = 3,

You should return the following matrix:
[
 [ 1, 2, 3 ],
 [ 8, 9, 4 ],
 [ 7, 6, 5 ]
]


Difficulty: Medium

Solution notes:

The matrix will be of dimension n x n.
My strategy was to build the matrix inside out.
For example, given n = 3, I would first start with [[9]].
Then add a list
[8]
[9]
And continously turn + zip the matrix
[9, 8]
and then add another list
[6, 7]       [9, 6]       [4, 5]      [8, 9, 4]       [1, 2, 3]
[9, 8]  ->   [8, 7]  ->   [9, 6]  ->  [7, 6, 5]  ->   [4, 5, 6]
                          [8, 7]                      [7, 8, 9]

Until I finally place the 1.

O(n) time
O(1) space
'''

def generate_matrix(n):
  if n == 0:
    return []
  last_written = pow(n,2)   # keep track of the last number we wrote to matrix
  result = [[pow(n,2)]]     # start with [n^2]
  while last_written > 1:   # as long as we haven't written the last 1
    result = [list(x)[::-1] for x in zip(*result)]    # * is Python's unpacking operator for list arguments. foo(*[1,2]) -> foo(1, 2)
    size = len(result[0])                             # size of new list
    new_row = [last_written-size+i for i in xrange(size)] # add another row
    result.insert(0, new_row)
    last_written -= size
  return result
