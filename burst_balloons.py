# Andy Yu
'''
There are a number of spherical balloons spread in two-dimensional space. 
For each balloon, provided input is the start and end coordinates of the horizontal diameter. 
Since it's horizontal, y-coordinates don't matter and hence the x-coordinates of start and end of the diameter suffice. 
Start is always smaller than end. There will be at most 10^4 balloons.

An arrow can be shot up exactly vertically from different points along the x-axis. 
A balloon with xstart and xend bursts by an arrow shot at x if xstart ≤ x ≤ xend. 
There is no limit to the number of arrows that can be shot. 
An arrow once shot keeps travelling up infinitely. 
The problem is to find the minimum number of arrows that must be shot to burst all balloons.

Example:
Input:
[[10,16], [2,8], [1,6], [7,12]]

Output:
2

Explanation:
One way is to shoot one arrow for example at x = 6 (bursting the balloons [2,8] and [1,6]) and another arrow at x = 11 (bursting the other two balloons).

Difficulty: Medium

Solution notes:
Greedy solution. First sort the balloons by their ending point.
Choose the balloon that ends first, and remove all the balloons that overlap with that one.
Then we choose the next balloon that ends first, and remove all the balloons that overlap.
We repeat this process until we have popped all the balloons.
The idea is that when looking at the balloon that ends first, we can safely shoot an arrow at its ending point and have that be in the optimal solution.
This is because since we are shooting the balloon that ends first, we do not run the risk of "missing" any balloons.
Furthermore, shooting the balloon at its end point guarantees popping the most other balloons.

O(nlogn) time
O(1) space
'''

def findMinArrowShots(self, points):
  if not points:
      return 0
  points.sort(key=lambda x:x[1])
  count = 1
  first_end = points.pop(0)[1]
  for point in points:
      if point[0] > first_end:
          first_end = point[1]
          count += 1
  return count
