# Andy Yu
'''
Given an array containing n distinct numbers taken from 0, 1, 2, ..., n, find the one that is missing from the array.

For example,
Given nums = [0, 1, 3] return 2.
Given nums = [1, 0] return 2.
Given nums = [2, 1] return 0.

Note:
Your algorithm should run in linear runtime complexity. Could you implement it using only constant extra space complexity?
Difficulty: Easy - Medium

Solution notes:

This was my initial solution, O(n) time - but it's still slow.

def missing_number(nums):
  nums = sorted(nums)
  iterator = 0
  for num in nums:
      if num != iterator:
          return iterator
      iterator += 1
  return iterator


Here's a clever one line math solution:

def missing_number(nums):
    return len(nums) * (len(nums) + 1) / 2 - sum(nums)

This works on the principle that the sum of all number from 0 ... n is n*(n+1)/2, so if you then subtract the expected sum
from the calculated sum then you're left with the missing number.

O(n) time
O(1) space

'''
def missing_number(nums):
    return len(nums) * (len(nums) + 1) / 2 - sum(nums)
    