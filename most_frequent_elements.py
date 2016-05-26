# Andy Yu
'''
Given a non-empty array of integers, return the k most frequent elements.

For example,
Given [1,1,1,2,2,3] and k = 2, return [1,2].

Note: 
You may assume k is always valid, 1 ≤ k ≤ number of unique elements.
Your algorithm's time complexity must be better than O(n log n), where n is the array's size.

Difficulty: Easy

Solution notes:
Since Python's sorted() function is O(nlogn) time, our final solution is O(n + nlogn) or just O(nlogn) time.

O(nlogn) time
O(1) space
'''

def most_frequent(nums, k):
  elements = {}
  for num in nums:
      elements[num] = max(elements.get(num, 0) + 1, 1)
  return sorted(elements, key=elements.get, reverse=True)[:k]

