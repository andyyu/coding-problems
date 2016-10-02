# Andy Yu
'''
Given a non-negative integer n, count all numbers with unique digits, x, where 0 ≤ x < 10^n.

Example:
Given n = 2, return 91. (The answer should be the total numbers in the range of 0 ≤ x < 100, excluding [11,22,33,44,55,66,77,88,99])


Difficult: Easy

Solution Notes:
We could do this the naive way, which would be to iterate over every element from 0 to 10^n and check if each number contains unique digits.
Even the iterating over every element would take O(10^n) time, let alone the time required to check unique digits for each number.
We could also run a dynamic programming solution with memoization, meaning we keep track of every "unique digit" number and simply add digits to the end to create new entries.
It's also helpful that we know that n is the maximum # of digits of any number in the range 10^n.

A solution would look something like this. Unfortunately, the time and space complexity quickly get out of hand (O(n^2) time and space).
def count_numbers_with_unique_digits(n):
  nums = [[""]]
  for i in xrange(1, n+1):
    i_digit_set = []
    for num in nums[-1]:
      for i in xrange(10):
        if i == 0 and num == "":
          continue
        if str(i) not in num:
          i_digit_set.append(num + str(i))
    nums.append(i_digit_set)
  return len([num for group in nums for num in group])

It seems like the output follows a fairly typical mathematical pattern though.
The first set of unique digits would be [0, 1, 2, 3, 4, 5, 6, 7, 8, 9]
For every digit in that set (except for 0), we can add any additional number except for itself, resulting in 9*9 new digits.
Then for every "extra" digit up to n, we can add any additional digit to the numbers in the previous set except for those digits already in the numbers, which gives (10-n) choices.

O(n) time
O(n) space

'''
def count_numbers_with_unique_digits(n):
  counts = [9]
  if n == 0:
    return 1
  for i in xrange(1, n):
    if i >= 10:
      break
    counts.append(counts[-1]*(10-i))
  return sum(counts) + 1