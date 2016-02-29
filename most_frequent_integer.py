# Andy Yu
'''
Given a list of integers, find the most commonly occuring integer.
Difficulty: Easy

Solution notes:
O(n) time
O(n) space
python tricks op
'''

def frequent_integer(numlist):
  num_map = {}
  for num in numlist:
    num_map[num] = num_map.get(num, 0) + 1
  return max(num_map, key=num_map.get)
