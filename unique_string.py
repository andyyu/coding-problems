# Andy Yu
'''
implement an algorithm to determine if a string has all unique characters w/o additional data structures
Difficulty: Easy

Solution notes:
O(n^2) / O(n) time
O(1) / O(1) space
2 solutions are listed below (the first is naive). 
'''

import sys
def check_unique(string): #time complexity of N^2
  for char in string:
    remaining = string[:string.find(char)] + string[string.find(char)+1:]
    if char in remaining:
      return False
  return True

def improved_check_unique(string): #time complexity of N (or technically O(1))
  if len(string) > 128: #length of ASCII alphabet
    return False
  flags = [0] * 128
  for char in string:
    if flags[ord(char)] == 1:
      return False
    else:
      flags[ord(char)] = 1
  return True