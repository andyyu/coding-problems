# Andy Yu
'''
Given positive integers a and b, return a^b.
Difficulty: Easy

Solution notes:
O(logn) time
O(1) space
'''

def power(a, b):
  if b == 0:
    return 1
  elif (b % 2 == 0):
    return power(a, b/2)*power(a, b/2)
  else:
    return a*power(a, b/2)*power(a, b/2)
