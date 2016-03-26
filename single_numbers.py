# Andy Yu
'''
Given an array of numbers nums, in which exactly two elements appear only once and all the other elements appear exactly twice. 
Find the two elements that appear only once.

For example:
Given nums = [1, 2, 1, 3, 2, 5]
return [3, 5]

Difficulty: Medium

Solution notes:
Immediate naive implementation would be to store encountered values in a data structure.
This would result in linear time/space complexity, but can we also do it in constant space complexity?

# O(n) space solution using a map
def single_num(nums):
  encountered = {}
  for num in nums:
      encountered[num] = encountered.get(num, 0) + 1
  return sorted(encountered, key = encountered.get)[:2]

Better solution - use bit manipulation!
O(n) time
O(1) space
'''

def single_num(nums):
  bit_field = 0
  a = 0
  b = 0
  for num in nums:
      # by XOR'ing a running bitfield by each number, we effectively cancel out the duplicate numbers and leave 0^a^b
      # where a and b must be the elements that occur once
      bit_field ^= num 
  mask = 1
  # now get the first 1 in bit_field to find a and b (the first 1 will be the first unique 1 since we XOR'd a and b)
  while (bit_field & mask == 0):
      mask = mask << 1
  # same thing as bit_field, but now we can separate a and b into their own fields using our mask, duplicate elements once again cancel each other out
  for num in nums:
      if num & mask:
          a ^= num
      else:
          b ^= num
  return [a, b]

