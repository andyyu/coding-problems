# Andy Yu
'''
Given an array S of n integers, are there elements a, b, c in S such that a + b + c = 0? Find all unique triplets in the array which gives the sum of zero.

Note: The solution set must not contain duplicate triplets.

For example, given array S = [-1, 0, 1, 2, -1, -4],

A solution set is:
[
  [-1, 0, 1],
  [-1, -1, 2]
]

Difficult: Medium

Solution Notes:
Sort list, then use 2 pointers to cover every combination. See 3_sum_closest for more explanation.

O(n^2) time
O(1) space
'''
def threeSum(self, nums):
  res = []
  sorted_list = sorted(nums)
  for left in xrange(0, len(nums)-2):
    mid = left + 1
    right = len(nums) - 1
    while mid < right:
      new_list = [sorted_list[left], sorted_list[mid], sorted_list[right]]
      s = sum(new_list)
      if s > 0:
        right -= 1
      elif s < 0:
        mid += 1
      else:
        if new_list not in res: 
          res.append(new_list)
        mid += 1
  return res

