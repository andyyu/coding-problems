# Andy Yu
'''
Given an array of non-negative integers, you are initially positioned at the first index of the array.
Each element in the array represents your maximum jump length at that position.
Determine if you are able to reach the last index.

For example:
A = [2,3,1,1,4], return true.

A = [3,2,1,0,4], return false.


Difficulty: Easy

Solution notes:
If you can jump from any particular index -> the last index, then we can just consider that index the new "end",
since we know once we get to that point we can reach the last index for sure.
Basic idea is to iterate from the end of the list to the front, starting with the "end" at the last index and
updating the "end" everytime we reach a new index that is able to reach the current "end".

O(n) time
O(1) space

'''
def can_jump(nums):
  if len(nums) == 0 or len(nums) == 1:
      return True
  end = len(nums) - 1
  distance = 1
  while end - distance > 0:
      if nums[end-distance] >= distance:
          end = end - distance
          distance = 1
      else:
          distance += 1
  if nums[0] < distance:
      return False
  else:
      return True