# Andy Yu
'''
Given a set of distinct integers, nums, return all possible subsets.

Note:
Elements in a subset must be in non-descending order.
The solution set must not contain duplicate subsets.
For example,
If nums = [1,2,3], a solution is:

[
  [3],
  [1],
  [2],
  [1,2,3],
  [1,3],
  [2,3],
  [1,2],
  []
]

Difficulty: Medium

Solution notes:
recursion
O(n^2) time
O(n) space

There is also a very clever iterative solution - O(2^n) time complexity though.
def subsets(self, nums):
    res = [[]]
    for num in sorted(nums):
        res += [item+[num] for item in res]
    return res
'''
def subsets(nums):
  ret = []
  recursive(sorted(nums), 0, [], ret)
  return ret

def recursive(nums, index, prefix, ret):
    ret.append(prefix)
    for i in xrange(index, len(nums)):
        recursive(nums[0:i]+nums[i+1:len(nums)], i, prefix + [nums[i]], ret) 