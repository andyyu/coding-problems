# Andy Yu
'''
Given an array with n objects colored red, white or blue, 
sort them so that objects of the same color are adjacent, 
with the colors in the order red, white and blue.

Here, we will use the integers 0, 1, and 2 to represent the color red, white, and blue respectively.

You are not allowed to use the library's sort function for this problem.


Difficulty: Medium

Solution notes:

Dutch-flag problem

My first thought was to iterate over the array twice. 
The first time I would count all the number of 0s, 1s, and 2s.
The second time I would populate the array with the proper number of 0s, 1s, and 2s in order.
To improve on this, I devised a way to do it in one pass using a variation of a partition algorithm used in quicksort.
The idea is that we keep a running index of where the next 0 and the next 1 should go.
Then, we iterate over every number and first replace it with 2, then depending on what number we replaced,
add an extra 0 and/or 1 at the zero index / one index and increment.

O(n) time
O(1) space
'''

def sort_colors(nums):
  zero_index = one_index = 0
  for i in xrange(len(nums)):
    temp = nums[i]
    nums[i] = 2
    if temp < 2:
        nums[one_index] = 1
        one_index += 1
    if temp == 0:
        nums[zero_index] = 0
        zero_index += 1