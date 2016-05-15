# Andy Yu
'''
The count-and-say sequence is the sequence of integers beginning as follows:
1, 11, 21, 1211, 111221, ...

1 is read off as "one 1" or 11.
11 is read off as "two 1s" or 21.
21 is read off as "one 2, then one 1" or 1211.
Given an integer n, generate the nth sequence.

Note: The sequence of integers will be represented as a string.

Difficulty: Easy

Solution notes:
O(n) time
O(1) space
'''

def count_and_say(n):
  s = '1'
  for i in xrange(n-1):
    start = s[0]
    temp = ''
    count = 0
    for num in s:
      if start == num:
        count += 1
      else:
        temp += str(count)+start
        start = num
        count = 1
    temp += str(count)+num
    s = temp
  return s
        