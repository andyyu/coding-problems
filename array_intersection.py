# Andy Yu
'''
Given two arrays, write a function to compute their intersection.

Example:
Given nums1 = [1, 2, 2, 1], nums2 = [2, 2], return [2].

Note:
Each element in the result must be unique.
The result can be in any order.

Difficulty: Easy

Solution notes:

Using a list comprehension and the properties of a set, we can do this in 1 line.
Iterate through all elements in nums1, check if it's nums2, then convert that list into a set (removing dupes), then back into a list for the proper output.

O(n) time 
O(1) space

'''
def intersection(nums1, nums2):
  return list(set([i for i in nums1 if i in nums2]))
