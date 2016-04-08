# Andy Yu
'''
The gray code is a binary numeral system where two successive values differ in only one bit.

Given a non-negative integer n representing the total number of bits in the code, print the sequence of gray code. 
A gray code sequence must begin with 0.

For example, given n = 2, return [0,1,3,2]. Its gray code sequence is:

00 - 0
01 - 1
11 - 3
10 - 2

For a given n, a gray code sequence is not uniquely defined.
For example, [0,2,3,1] is also a valid gray code sequence according to the above definition.

Difficulty: Medium

Problem solutions:
First, we should write out an example sequence of gray code.
n         gc
0         0
1         0 1
2         0 1 11 10
3         0 1 11 10 110 111 101 100

Do you see a pattern? As n increases, the gray code sequence corresponding contains the gray code sequence
from n-1, then doubles the sequence by adds on a 1 bit to the front of every previous bit string, 
but in reverse!
n=2 : 00 01 11 10
n=3 : 00 01 11 10 
      +
      110 111 101 100 (this is n=2's sequence reversed, with an extra 1 bit in front)

With this in mind, a solution is simple (we can also speed it up by continously
building on the last calculated gray code sequence - dynamic programming)

O(n) time
O(1) space

dp
'''

def gray_code(n):
  ret = [0]
  for i in xrange(n):
    ret.extend(int(math.pow(2, i) + x) for x in reversed(ret))
  return ret
        
