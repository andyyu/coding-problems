# Andy Yu
'''
Given a string S, find the longest palindromic substring in S. 
You may assume that the maximum length of S is 1000, and there exists one unique longest palindromic substring.

Difficulty: Medium

Solution notes:

Idea is that for every extra letter that we add, the length of the longest palindrome in the new string can only be as great as the longest palindrome in the old string +1 or +2.
Case 1: "abcc" + "c" -> "abcc"
  Longest palindrome = 2 -> 3
Case 2: "abcb" + "a" -> "abcba"
  Longest palindrome = 3 -> 5
Therefore, all we have to do is add 1 letter each time and check if either the substring containing the last letter, of length (largest_so_far+1 and largest_so_far+2)
are palindromes.

O(n^2) time
O(1) space
'''

def longest_palindrome(s):
  if len(s) == 0:
      return 0
  max_palindrome = 1
  start = 0
  for i in xrange(1, len(s)):
    if i > max_palindrome and is_palindrome(s[i-max_palindrome-1:i+1]):
      start = i-max_palindrome-1
      max_palindrome += 2
    elif is_palindrome(s[i-max_palindrome:i+1]):
      start = i-max_palindrome
      max_palindrome += 1
  return s[start:start+max_palindrome]

def is_palindrome(s):
  return s == s[::-1]