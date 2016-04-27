# Andy Yu
'''
Find the total area covered by two rectilinear rectangles in a 2D plane.

https://leetcode.com/static/images/problemset/rectangle_area.png

Rect 1: bottom left hand point (A, B), top right hand point (C, D)
Rect 2: bottom left hand point (E, F), top right hand point (G, H)

Each rectangle is defined by its bottom left corner and top right corner as shown in the figure.

Rectangle Area
Assume that the total area is never beyond the maximum possible value of int.


Difficulty: Medium

Solution notes:


O(n) time
O(1) space
'''

def computeArea(A, B, C, D, E, F, G, H):
  overlap_width = max(min(C,G)-max(A,E), 0)
  overlap_height = max(min(D,H)-max(B,F), 0)
  return abs((A-C)*(B-D)) + abs((E-G)*(F-H)) - abs(overlap_width * overlap_height)



