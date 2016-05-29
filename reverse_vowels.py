# Andy Yu
'''
Write a function that takes a string as input and reverse only the vowels of a string.

Example 1:
Given s = "hello", return "holle".

Example 2:
Given s = "supercilious", return "suporcilieus".


Solution Notes:

O(n) time
O(1) space
'''

def reverse_vowels(s):
  left = 0
  right = len(s)-1
  vowels = 'aeiou'
  while left != right:
    print left
    print right
    if s[left] not in vowels:
      left += 1
    elif s[right] not in vowels:
      right -= 1
    else:
      swap(left, right)
  return s