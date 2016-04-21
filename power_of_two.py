# Andy Yu
'''
Given an integer, write a function to determine if it is a power of two.

Difficulty: Very Easy

Solution notes:
My initial thoughts was to simply keep dividing the integer by 2 until it reaches 1 or less.
If it reaches 1 it is a power of 2, if it instead becomes less than 1 without reaching 1 then it is not.

def is_power_of_2(num):
  while n > 1:
    n /= 2.0    # keep it a float, or else Python will round
  return True if n == 1 else False

This solution takes O(n) time when the integer is ~2^n.

If this function was planned to be run multiple times, it would be faster to have a running dictionary
of found powers of 2, and most cases would take less than O(n) time (even as fast as O(1) for direct access).
This way, if the integer ever reached a previously found power of 2 (checking in the dictionary each time)
while it was being divided by 2, then we can stop there and conclude that it is also a power of 2.

The last solution involves bit manipulation.
Since we know the binary representation of any power of two is a solitary 1 followed by any number of 0s,
we can simply check if the binary n is of that form.

This solution is
O(1) time
O(1) space
'''

def is_power_of_2(num):
  return not (n == 0) and not (n & n-1)
