# Andy Yu
'''
Write a function that takes a string as input and reverse only the vowels of a string.

Example 1:
Given s = "hello", return "holle".

Example 2:
Given s = "supercilious", return "suporcilieus".

Solution Notes:

We use two pointers, starting at each end of the string. 
While the left pointer is less than the right pointer, we check if they are both vowels and swap, or move pointers if they are not on a vowel.

My original iteration used a vowel "string": 'aeiouAEIOU' and checked if s[left/right] was 'in' the string - slow!
and "swap" would rebuild the string using slices each time (s = s[:left] + s[right] + s[left+1:right] + s[left] + s[right+1:])
But those both slow the function down immensely.
Instead, look at my final solution to see my optimizations.

O(n) time
O(1) space
'''

def reverseVowels(self, s):
  if not s:   # empty string
    return '' 
  left = 0
  right = len(s)-1
  vowels = set(['a', 'e', 'i', 'o', 'u', 'A', 'E', 'I', 'O', 'U'])   # sets have avg constant access time 
  s = list(s)   # convert to list to make swap much faster (strings are immutable, so you'd have to rebuild the string each time which is very costly)
  while left < right:
    if s[left] in vowels and s[right] in vowels:
      s[left], s[right] = s[right], s[left]   # swap vowels
      left += 1
      right -= 1
    if s[left] not in vowels:
      left += 1
    if s[right] not in vowels:
      right -= 1
  return ''.join(s)   # return a string