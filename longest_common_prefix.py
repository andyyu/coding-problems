# Andy Yu
'''
Write a function to find the longest common prefix string amongst an array of strings.

Difficulty: Easy

Solution notes:
Taking advantage of Python's builtin all() function, which returns true if a condition is true for all elements in a list.

O(n*m) time where n is the number of words and m is the length of the longest prefix
O(1) space
'''
def longestCommonPrefix(self, strs):
  if not strs:
    return ""
  shortest = min(len(s) for s in strs)
  ret = ""
  for i in xrange(shortest):
    letter = strs[0][i]
    if all(str[i] == letter for str in strs):
      ret += letter
    else:
      break
  return ret