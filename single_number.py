# Andy Yu
'''
Given an array of integers, every element appears twice except for one. Find that single one.

Difficulty: Easy - Medium

Solution notes:

This solution uses bit manipulation - bitwise XOR is 0 when both inputs are 1, otherwise it is 1.
We can use this idea to essentially "cancel out" every duplicate element. 
If we XOR every element in the array, the elements that appear twice will zero out each other and only the single element will remain.


O(n) time
O(1) space

'''
def single_number(nums):
  bit_map = 0
  for num in nums:
      bit_map ^= num
  return int(bit_map)

