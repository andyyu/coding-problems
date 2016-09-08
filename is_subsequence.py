# Andy Yu
'''
Given a string s and a string t, check if s is subsequence of t.

You may assume that there is only lower case English letters in both s and t. 
t is potentially a very long (length ~= 500,000) string, and s is a short string (<=100).

A subsequence of a string is a new string which is formed from the original string by deleting some (can be none) of the characters without disturbing the relative positions of the remaining characters. 
(ie, "ace" is a subsequence of "abcde" while "aec" is not).

Example 1:
s = "abc", t = "ahbgdc"

Return true.

Example 2:
s = "axc", t = "ahbgdc"

Return false.

Difficult: Medium

Solution Notes:

Fun short Python one:
def is_subsequence(s, t):
  t = iter(t)
  return all(c in t for c in s)

The above works since iter() returns an iterator object which only yields objects not yielded previously.
Basically, "c in t" will first begin iterating through the first letters in t, and for the next c it will only yield the letters it didn't yield in previous iterations.

O(n) time
O(1) space
'''
def is_subsequence(s, t):
  if len(s) > len(t): # if s is longer, can not be a subsequence of t
    return False
  if len(s) == 0:     # if s is of length 0, it must be a subsequence of t
    return True
  pos = 0             # keep track of which letter we are checking
  for c in t:         # iterate through all letters in t
    if s[pos] == c:   # if the letter in t corresponds to the letter in s we are checking, increment pos
      pos += 1
      if pos == len(s): # check if all letters in s have been found
          return True
  return False

''' Alternatively: use a list and pop off letters instead of iterating a position
def is_subsequence(s, t):
  if len(s) > len(t):
    return False
  if len(s) == 0:
    return True
  s = list(s)
  for c in t:
    if not s:
      return True
    if s[0] == c:
      s.pop(0)
  return False

'''
  

