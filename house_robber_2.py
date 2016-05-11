# Andy Yu
'''
Note: This is an extension of House Robber.

After robbing those houses on that street, the thief has found himself a new place for his thievery so that he will not get too much attention. 
This time, all houses at this place are arranged in a circle. 
That means the first house is the neighbor of the last one. 
Meanwhile, the security system for these houses remain the same as for those in the previous street.

Given a list of non-negative integers representing the amount of money of each house, determine the maximum amount of money you can rob tonight without alerting the police.

Difficulty: Medium

Solution notes:
O(n) time
O(1) space
'''

def house_robber(nums):
  if not nums:
    return 0
  max_money = [0]*len(nums)
  except_first = [0]*(len(nums)-1)
  for i in xrange(len(nums)):
    if i == 0:
      max_money[0] = nums[0]
    elif i == 1:
      max_money[1] = max(nums[0], nums[1])
      except_first[0] = nums[1]
    elif i == 2:
      max_money[i] = max(nums[i]+except_first[i-2], max_money[i-1])
      except_first[1] = max(nums[1], nums[2])
    else:
      max_money[i] = max(nums[i]+except_first[i-2], max_money[i-1])
      except_first[i-1] = max(nums[i]+except_first[i-3],except_first[i-2])
  return max_money[-1]