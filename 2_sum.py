# Andy Yu
'''
Given an array of integers, return indices of the two numbers such that they add up to a specific target.

You may assume that each input would have exactly one solution.

Example:
Given nums = [2, 7, 11, 15], target = 9,

Because nums[0] + nums[1] = 2 + 7 = 9,
return [0, 1].

Difficulty: Easy

Solution notes:

- First iteration - 
def two_sum(nums, target):
  for i, num in enumerate(nums):
    if target-num in nums[i+1:len(nums)]:
      return [i, nums.index(target-num, i+1)]

This solution involves iterating over every number in the array and checking if the number required to sum to target exists in the array.
Better than O(n^2) since as it goes through the list, it only searches the remaining numbers.
Short code, but horribly inefficient.

- Second iteration -

def twoSum(self, nums, target):
  ascending = sorted(nums)
  left, right = 0, len(nums)-1
  while left < right:
    current = ascending[left] + ascending[right]
    if current == target:
      if ascending[left] == ascending[right]:
        first = nums.index(ascending[left])
        second = nums.index(ascending[right], first+1)
      else:
        first = nums.index(ascending[left])
        second = nums.index(ascending[right])
      return [first, second]
    if current < target:
      left += 1
    else:
      right -= 1

This solution was to improve upon the speed of the 2nd by not having to create a dictionary.
Strategy was to sort first, then search using two left and right pointers. 
The only problem is we have to return the indices of the numbers in the old array, so we have to account for that.
In the end, all that index() calls slows our O(n) solution to only beat 44% of solutions on leetcode.
We can do better than that.

- Third solution -
def two_sum(nums, target):
  num_dict = {}
  for num in nums:
    num_dict[num] = max(num_dict.get(num, 0)+1, 1)
  for i, num in enumerate(nums):
    if target-num in num_dict:
        if target-num == num and not num_dict[num] > 1:
            continue
        return [i, nums.index(target-num, i+1)]

This solution acts on the same principle as the second, only we first initialize a dictionary to hold the values so that
for every number the searching takes O(1) time, reducing our time complexity of the total solution to O(n).
The only problem is this dictionary creation takes a large chunk of time. We also use an extra O(n) space every time. Inefficient.

- Final solution -
Listed below.
We improved on the 3rd solution by only adding encountered numbers into the dictionary.
This runs on the premise that when we hit a number that's part of the solution, 
its matching sum "pair" must have either already been encountered (and is in the dict / map),
or it matching number will be encountered in the future (and will find this current number in the map).

O(n) time
O(n) space

'''
def two_sum(nums, target):
  d = {}
  for i, num in enumerate(nums):
    if target-num in d:
        return [d[target-num], i]
    else:
        d[num] = i
