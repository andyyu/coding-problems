# Andy Yu
'''
Given an integer array, find three numbers whose product is maximum and output the maximum product.

Example 1:
Input: [1,2,3]
Output: 6
Example 2:
Input: [1,2,3,4]
Output: 24
Note:
The length of the given array will be in range [3,104] and all elements are in the range [-1000, 1000].
Multiplication of any three numbers in the input won't exceed the range of 32-bit signed integer.

Difficulty: Easy

Problem solutions:
This problem would be very trivial if not for the possibility of negative integers.
We know that besides the obvious choice of (the product of the 3 largest numbers),
we must also consider the scenario of (the product of the two smallest (negative) numbers, and the largest positive number).
We can simply consider both scenarios in one pass, 
keeping track of the two most negative numbers and the three most positive numbers.

O(n) time
O(1) space
'''

def maximumProduct(nums):
  largest = [float('-inf')] # largest 3, populate with default value so it's not an empty list
  smallest = [float('inf')] # smallest 2
  for num in nums:
    if num > largest[-1]: # maintain last in list as the smallest of the largest 3
      if len(largest) == 3: # if already 3 numbers, delete one to make room for the new
        del largest[-1]
      largest.append(num)
      largest.sort(reverse=True)
    if num < smallest[-1]: # maintain last in list as the larger of the two
      if len(smallest) == 2:
        del smallest[-1]
      smallest.append(num)
      smallest.sort()
  return max(reduce(lambda x, y: x * y, largest, 1), largest[0]*smallest[1]*smallest[0]) # pick the greater of the two scenarios
  # Note: the above reduce + lambda was for fun, largest[2]*largest[1]*largest[0] would work just as well.

if __name__ == '__main__':
  print maximumProduct([5, 2, -10, -6, 3])
