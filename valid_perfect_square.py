# Andy Yu
'''
Given a positive integer num, write a function which returns True if num is a perfect square else False.

Note: Do not use any built-in library function such as sqrt.

Example 1:

Input: 16
Returns: True
Example 2:

Input: 14
Returns: False

Difficult: Easy

Solution Notes:
Use binary search.

O(logn) time
O(1) space

'''
def is_perfect_square(num):
  low = 1
  high = num
  while low <= high:
    mid = (low+high)/2
    if mid**2 > num:
      high = mid-1
    elif mid**2 < num:
      low = mid+1
    else:
      return True
  return False