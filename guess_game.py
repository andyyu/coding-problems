# Andy Yu
'''
We are playing the Guess Game. The game is as follows:

I pick a number from 1 to n. You have to guess which number I picked.

Every time you guess wrong, I'll tell you whether the number is higher or lower.

You call a pre-defined API guess(int num) which returns 3 possible results (-1, 1, or 0):

-1 : My number is lower
 1 : My number is higher
 0 : Congrats! You got it!
Example:
n = 10, I pick 6.

Return 6.

Difficult: Easy 

Solution Notes:
Binary search algorithm.

O(logn) time
O(1) space
'''
def guess_number(n):
  first = 1
  last = n
  while first < last:
      mid = (first+last)/2
      res = guess(mid)
      if res == 0:
          break
      elif res == 1:
          first = mid+1
      else:
          last = mid-1
  return (first+last)/2

