# Andy Yu
'''
Find the largest sum possible from an array of integers.
Difficulty: Medium

Solution notes:
dynamic programming
O(n) time
O(1) space
'''

def findLargestSum(arr):
  sum_so_far = arr[0]
  largest_sum = arr[0]
  for num in xrange(len(arr)):
    if num == 0:
      continue
    sum_so_far = max(sum_so_far + arr[num], arr[num])
    largest_sum = max(largest_sum, sum_so_far)
  return largest_sum
