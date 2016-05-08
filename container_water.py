# Andy Yu
'''
Given n non-negative integers a1, a2, ..., an, where each represents a point at coordinate (i, ai). 
n vertical lines are drawn such that the two endpoints of line i is at (i, ai) and (i, 0). 
Find two lines, which together with x-axis forms a container, such that the container contains the most water.

Note: You may not slant the container.

Difficulty: Medium

Solution notes:

The naive solution would just be to iterate through all the elements and for each one, check every other element and keep track of the max water able to be held.
This would be O(n^2) time. We can do better than that.
The biggest problem to a more efficient solution is that it's very possible to skip "over" one of the two lines needed for the solution when searching.
What I mean is, for example, we made a container using a very tall line and a short line, we would only be able to hold as much water as the short line x width.
Therefore, in a poor solution it's very possible to presume that neither line will be in the solution when in reality we just never checked the very tall line with it's correct partner.

In our solution, I use two pointers, a "left" and a "right" pointer starting from the beginning and the end of the array, respectively.
We iterate over the lines, moving the left pointer rightward and the right pointer leftward until they meet, at which point we've iterated over all the lines.
To solve the problem addressed above, we can abuse one important observation.
The only time that a line essential to the solution can be accidentally passed over is when the other line it's being compared to is shorter than it.
If we compare a line with one taller than itself, and we record the water it can hold at that point, as long as our two pointers are moving together that line will NEVER be able to hold more water than at that point.
Therefore, if we only increment our pointer if it's pointing at the smaller line, we will therefore never "pass over" a line without checking its full potential.

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