# Andy Yu
'''
Write an algorithm to determine if a number is "happy".

A happy number is a number defined by the following process: 
Starting with any positive integer, replace the number by the sum of the squares of its digits, 
and repeat the process until the number equals 1 (where it will stay), 
or it loops endlessly in a cycle which does not include 1. 
Those numbers for which this process ends in 1 are happy numbers.

Example: 19 is a happy number

1^2 + 9^2 = 82
8^2 + 2^2 = 68
6^2 + 8^2 = 100
1^2 + 0^2 + 0^2 = 1

Difficulty: Easy

Solution notes:

This problem is just cycle detection. If we ever hit the same number again, then we know we'll just be going
in a cycle -> can't be a happy number.
The below solution is a pretty basic solution involving saving previously encountered numbers and returning false
if we ever get the same number as before (cycle).

def is_happy(n):
  prev = set()
  while True:
    if n in prev:
        return False
    else:
        prev.add(n)
    res = sum([int(x) ** 2 for x in str(n)])
    if res == 1:
        return True
    else:
        n = res

This, however, takes a great deal of space depending on how many numbers we go through before encountering a loop.
We can improve upon this by using Floyd's cycle-detecting algorithm (google it for more details!)
The solution is listed below.

O(1) space
'''

def next(self, num):
  return sum([int(x) ** 2 for x in str(num)])
    
def isHappy(self, n):
  slow = self.next(n)
  fast = self.next(slow)
  while True:
      slow = self.next(slow)
      fast = self.next(self.next(fast))
      if slow == 1 or fast == 1:
          return True
      elif slow == fast:
          return False