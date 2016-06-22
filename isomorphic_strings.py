# Andy Yu
'''
Given two strings s and t, determine if they are isomorphic.

Two strings are isomorphic if the characters in s can be replaced to get t.

All occurrences of a character must be replaced with another character while preserving the order of characters. No two characters may map to the same character but a character may map to itself.

For example,
Given "egg", "add", return true.

Given "foo", "bar", return false.

Given "paper", "title", return true.

Note:
You may assume both s and t have the same length.

Difficult: Easy

Solution Notes:
Clever solution (not mine) - 
def is_isomorphic(s, t):
  return len(set(zip(s, t))) == len(set(s)) == len(set(t))

O(n) time
O(1) space
'''
def is_isomorphic(s, t):
  d1 = {}
  d2 = {}
  for i, j in zip(s, t):
    if d1.get(i, j) != j:
      return False
    if d2.get(j, i) != i:
      return False
    else:
      d1[i] = j
      d2[j] = i
  return True

