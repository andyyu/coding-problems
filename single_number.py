# Andy Yu
'''
Given an array of integers, every element appears twice except for one. Find that single one.

Difficulty: Easy - Medium

Solution notes:
O(n) time
O(1) space

'''
def single_number(nums):
  bit_map = 0
  for num in nums:
      bit_map ^= num
  return int(bit_map)

