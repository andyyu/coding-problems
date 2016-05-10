# Andy Yu
'''
You are a professional robber planning to rob houses along a street. 
Each house has a certain amount of money stashed.
The only constraint stopping you from robbing each of them is that adjacent houses have security system connected and it will automatically contact the police if two adjacent houses were broken into on the same night.

Given a list of non-negative integers representing the amount of money of each house, 
determine the maximum amount of money you can rob tonight without alerting the police.

Difficulty: Easy

Solution notes:

Approach this with dynamic programming.
When there's just 1 house, max money = money in that one house.
When there's two houses, max money = max of house1/house2.
Every time we add another "potential" house on that street, we have two choices.
The best answer will either rob that house or not - if we rob that house, then we can't rob the house before it.
Therefore, we only need to check the greater of two choices:
Rob the newly added (last) house, and add that money to the max_money we knew in the n-2 case (because now we can't rob the 2nd to last house).
Or don't rob the newly added house, and then the max_money would be the same as in the n-1 case.

O(n) time
O(1) space
'''
def house_robber(nums):
  if not nums:
    return 0
  max_money = [0]*len(nums)
  for i in xrange(len(nums)):
    if i == 0:
      max_money[0] = nums[0]
    elif i == 1:
      max_money[1] = max(nums[0], nums[1])
    else:
      max_money[i] = max(nums[i] + max_money[i-2], max_money[i-1])
  return max_money[-1]
        
  