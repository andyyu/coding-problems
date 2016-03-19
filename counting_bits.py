# Andy Yu
'''
Given a non negative integer number num. 
For every numbers i in the range 0 ≤ i ≤ num, calculate the number of 1's in their binary representation. 
Return in an array.

Example:
For num = 5 you should return [0,1,1,2,1,2].
Difficulty: Medium

Solution notes:
O(n) time
O(n) space
dynamic programming

Trick: find the pattern in 
  00
  01
  10
  11
 100 (looks familiar to index 0, huh?)
 101 (1 + index[1])
 110 (1 + index[2])
 111 (1 + index[3])
1000 (reset)
1001
'''

def calculate_binary(num):
  result = []
  bit_length = 1 # keep track of how many bits needed to represent the current num
  for i in xrange(num+1):
      if i == 0 or i == 1:  # first two cases
          result.append(i)
      else:
          if result[i-1] == binary_length:  # this means all 1's, so must increase bit length
              bit_length += 1
              result.append(1)  # leading 1 and rest 0s
          else:
              set_length = int(math.pow(2, (bit_length-1))) # calculate how many numbers have this bit_length
              result.append(1 + result[i-set_length]) # look at pattern above
  return result

