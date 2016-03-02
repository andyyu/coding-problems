# Andy Yu
'''
Reverse a string.
Difficulty: Very Easy

Solution notes:
O(n) time
O(n) space
3 solutions are listed below. 
Note: Python strings are immutable
'''

def reverse_string_slice(string):
  return string[::-1]

def reverse_string_standard(string):
  rev = ""
  for i in range(len(string)-1, -1, -1):
    rev+= string[i]
  return rev

def reverse_string_reversed(string):
  return ''.join(reversed(string))