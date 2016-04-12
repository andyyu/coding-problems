# Andy Yu
'''
Find the contiguous subarray within an array (containing at least one number) which has the largest sum.

For example, given the array [−2,1,−3,4,−1,2,1,−5,4],
the contiguous subarray [4,−1,2,1] has the largest sum = 6.

Difficulty: Medium

Solution notes:
dynamic programming
O(n) time
O(1) space
'''

def maxSubArray(self, nums):
  max_subarray = [nums[0]]
  max_sum = nums[0]
  running_sum = max_sum
  running_subarray = max_subarray
  for i in xrange(1, len(nums)):
      if running_sum + nums[i] > nums[i]:
          running_sum += nums[i]
          running_subarray.append(nums[i])
      else:
          running_sum = nums[i]
          running_subarray = [nums[i]]
      if running_sum > max_sum:
          max_sum = running_sum
          max_subarray = running_subarray
  return max_subarray