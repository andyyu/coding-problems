# Andy Yu
'''
Given an array S of n integers, find three integers in S such that the sum is closest to a given number, target. 
Return the sum of the three integers. 
You may assume that each input would have exactly one solution.
    
For example, given array S = {-1 2 1 -4}, and target = 1.
The sum that is closest to the target is 2. (-1 + 2 + 1 = 2).

Difficulty: Medium

Solution notes:
O(n^2) time
O(1) space

'''
def three_sum_closest(nums, target):
  nums.sort()                                  # first, sort ascending
  closest = nums[0] + nums[1] + nums[2]        # initial placeholder
  for i in xrange(len(nums) - 2):              # iterate i through the 3rd to last value (j and k occupy the last two)
    j = i + 1                                  # start j at i+1
    k = len(nums) - 1                          # start k at the end
    while j < k:                               # j and k will move closer together until the closest value using that specific i is found
        temp = nums[i] + nums[j] + nums[k]     
        if temp == target:                     # target found
            return temp
        if abs(target-temp) < abs(target-closest):  # update closest value
            closest = temp
        if temp < target:                      # if calculated value is too small, move j right (increasing the value)
            j += 1
        else:                                  # if calculated value is too big, move k left (decreasing the value)
            k -= 1
  return closest

