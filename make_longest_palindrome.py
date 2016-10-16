# Andy Yu
'''
Given a string which consists of lowercase or uppercase letters, find the length of the longest palindromes that can be built with those letters.

This is case sensitive, for example "Aa" is not considered a palindrome here.

Note:
Assume the length of given string will not exceed 1,010.

Example:

Input:
"abccccdd"

Output:
7

Explanation:
One longest palindrome that can be built is "dccaccd", whose length is 7.

Difficulty: Easy

Solution notes:
O(n^2) time
O(n) space

'''
def longest_palindrome(s):
  count = 0
  letter_map = {}
  for i in s:
    c = letter_map.get(i, 0)
    if c == 1:
      count += 2
      letter_map[i] = 0
    else:
      letter_map[i] = 1
  if any(i == 1 for i in letter_map.values()):
    count += 1
  return count