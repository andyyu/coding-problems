# Andy Yu
'''
Given two integers n and k, return all possible combinations of k numbers out of 1 ... n.

For example,
If n = 4 and k = 2, a solution is:

[
  [2,4],
  [3,4],
  [2,3],
  [1,2],
  [1,3],
  [1,4],
]


Difficult: Medium

Solution Notes:
Backtracking iterative solution using a stack.

O(n^k) time
O(1) space
'''
def combine(n, k):
  res = []
  stack = []
  next = 1
  while True:
    if len(stack) == k:
      res.append(stack[:])
      stack.pop()
    if next > n:
      if not stack:
        return res
      last = stack.pop()
      next = last + 1
    else:
      stack.append(next)
      next += 1