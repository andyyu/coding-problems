# Andy Yu
'''
Given n non-negative integers a1, a2, ..., an, where each represents a point at coordinate (i, ai). 
n vertical lines are drawn such that the two endpoints of line i is at (i, ai) and (i, 0). 
Find two lines, which together with x-axis forms a container, such that the container contains the most water.

Note: You may not slant the container.

Difficulty: Medium

Solution notes:
O(n) time
O(1) space

'''
def max_water(height):
  left, right, width, max_water = 0, len(height) - 1, len(height) - 1, 0
  for i in range(width, 0, -1):
    if height[left] < height[right]:
      max_water = max(max_water, height[left] * i)
      left += 1
    else:
      max_water = max(max_water, height[right] * i)
      right -= 1
  return max_water