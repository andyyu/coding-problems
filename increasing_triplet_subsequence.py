# Andy Yu
'''
Given an unsorted array return whether an increasing subsequence of length 3 exists or not in the array.

Formally the function should:
Return true if there exists i, j, k 
such that arr[i] < arr[j] < arr[k] given 0 ≤ i < j < k ≤ n-1 else return false.
Your algorithm should run in O(n) time complexity and O(1) space complexity.

Examples:
Given [1, 2, 3, 4, 5],
return true.

Given [5, 4, 3, 2, 1],
return false.

Difficulty: Medium

Solution notes:
The solution is quite short, but more difficult conceptually than I first imagined.
For one, this checks for a matching -subsequence-. Do not make the naive mistake (like I did at first) of thinking the sequence had to be consecutive (that would be insanely trivial, after all).
Next, the idea that this solution is based off of is that we use two variables, small and big, to keep track of the entire "history" of the sequence as we iterate over it.
Big holds the smallest number that we've come across that MUST have a number before it that is smaller (making an increasing subsequence of 2).
Thus, once we hit a number that's bigger than that - there must be an increasing subsequence of length 3.
Small is basically used as a buffer to ensure that big gets updated whenever a smaller increasing subsequence comes along.

O(n) time
O(1) space
'''

def increasing_triplet(nums):
  small = big = float('inf')
  for n in nums:
    if n <= small:
      small = n
    elif n <= big:
      big = n
    else:
      return True
  return False