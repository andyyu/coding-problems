# Andy Yu
'''
Given an array of integers, find if the array contains any duplicates. 
Your function should return true if any value appears at least twice in the array, and it should return false if every element is distinct.

Difficult: Easy

Solution Notes:
Use the property of sets (unique). Alternatively, use a hash map to keep track of how many times elements appear.

def contains_duplicate(nums):
  dup_map = {}
  for element in nums:
    if element in dup_map:
      return True
    else:
      dup_map[element] = 1
  return False

O(n) time
O(1) space
'''
def contains_duplicate(nums):
  return len(nums) > len(set(nums))
  # return len(set(nums)) != len(nums)
  # return sorted(list(set(nums))) != sorted(nums)