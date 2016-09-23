# Andy Yu
'''
Given an array of integers with possible duplicates, randomly output the index of a given target number. You can assume that the given target number must exist in the array.

Note:
The array size can be very large. Solution that uses too much extra space will not pass the judge.

Example:

int[] nums = new int[] {1,2,3,3,3};
Solution solution = new Solution(nums);

// pick(3) should return either index 2, 3, or 4 randomly. Each index should have equal probability of returning.
solution.pick(3);

// pick(1) should return 0. Since in the array only nums[0] is equal to 1.
solution.pick(1);

Difficult: Easy 

Solution Notes:
Binary search algorithm.

O(logn) time
O(1) space
'''
class Solution(object):
  sorted_list = []
  def __init__(self, nums):
    Solution.sorted_list = sorted(nums)
    """
    
    :type nums: List[int]
    :type numsSize: int
    """
      

  def pick(self, target):
    length = len(Solution.sorted_list)
    lo = 0
    hi = length - 1
    while lo <= hi:
      mid = (lo+hi)/2
      if Solution.sorted_list[mid] == target:
        break
      if Solution.sorted_list[mid] < target:
        lo = mid+1
      else:
        hi = mid-1
    low_index = mid
    while low_index > 0 and Solution.sorted_list[low_index-1] == target:
      low_index-=1
    high_index = mid
    while high_index < (length-1) and Solution.sorted_list[high_index+1] == target:
      high_index+=1
    return random.randint(low_index, high_index)

