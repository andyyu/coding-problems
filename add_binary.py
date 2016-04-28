# Andy Yu
'''
Given two binary strings, return their sum (also a binary string).

For example,
a = "11"
b = "1"
Return "100".


Difficulty: Easy

Solution notes:

Bit of a cheat-y way to do it, use Python's in-built binary string <-> integer functions

Alternatively: recursive solution

def add_binary(a, b):
  if len(a)==0: return b
  if len(b)==0: return a
  if a[-1] == '1' and b[-1] == '1':
      return add_binary(add_binary(a[0:-1],b[0:-1]),'1')+'0'
  if a[-1] == '0' and b[-1] == '0':
      return add_binary(a[0:-1],b[0:-1])+'0'
  else:
      return add_binary(a[0:-1],b[0:-1])+'1'

'''
def add_binary(a, b):
  sum = int(a, 2) + int(b, 2)
  return bin(sum)[2:]           # bin(x) returns the binary string representation of an integer x, we cut off the leading '0b'