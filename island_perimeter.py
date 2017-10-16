# Andy Yu
'''
You are given a map in form of a two-dimensional integer grid where 1 represents land and 0 represents water. Grid cells are connected horizontally/vertically (not diagonally). The grid is completely surrounded by water, and there is exactly one island (i.e., one or more connected land cells). The island doesn't have "lakes" (water inside that isn't connected to the water around the island). One cell is a square with side length 1. The grid is rectangular, width and height don't exceed 100. Determine the perimeter of the island.

Example:

[[0,1,0,0],
 [1,1,1,0],
 [0,1,0,0],
 [1,1,0,0]]

Answer: 16
Explanation: The perimeter is the 16 yellow stripes in the image https://leetcode.com/static/images/problemset/island.png


Difficult: Easy

Solution Notes:
Very simple, just iterate through all the squares, then
check all 4 sides of each square and add one to the perimeter if there isn't a bordering "1" on that side.

O(n) time
O(1) space

'''

def islandPerimeter(grid):
    perimeter = 0
    for y, row in enumerate(grid):
        for x, square in enumerate(row):
            if square == 1:
                if y == 0 or grid[y-1][x] == 0:
                    perimeter += 1
                if y == len(grid)-1 or grid[y+1][x] == 0:
                    perimeter += 1
                if x == 0 or grid[y][x-1] == 0:
                    perimeter += 1
                if x == len(row)-1 or grid[y][x+1] == 0:
                    perimeter += 1
    return perimeter
