# Andy Yu
'''
Given a sorted array and a target value, return the index if the target is found. 
If not, return the index where it would be if it were inserted in order.

You may assume no duplicates in the array.

Here are few examples.
[1,3,5,6], 5 → 2
[1,3,5,6], 2 → 1
[1,3,5,6], 7 → 4
[1,3,5,6], 0 → 0
[1], 1 → 0

The naive implementation would be a simple linear search,
def search_insert(nums, target):
  index = 0
  while index != len(nums):
      if nums[index] >= target:
          break
      index += 1
  return index

this would give a pretty good time complexity of O(n). But can we do better?
What about a binary search?

Difficulty: Easy-Medium

Solution notes:
O(logn) time
O(1) space
'''
def search_insert(nums, target):
  if len(nums) == 0:
    return 0
  middle = len(nums)/2
  if target <= nums[middle]:
    return search_insert(nums[0:middle], target)
  else:
    return middle + search_insert(nums[middle+1:len(nums)], target)


        