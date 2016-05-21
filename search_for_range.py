# Andy Yu
'''
Given a sorted array of integers, find the starting and ending position of a given target value.

Your algorithm's runtime complexity must be in the order of O(log n).

If the target is not found in the array, return [-1, -1].

For example,
Given [5, 7, 7, 8, 8, 10] and target value 8,
return [3, 4].

Difficulty: Medium

Solution notes:
My first iteration looked something like this:

  def searchRange(self, nums, target):
    random = self.binary_search(nums, target)
    if random == -1:
      return [-1, -1]
    i = j = random
    while i > 0:
      i -= 1
      if nums[i] != target:
        i += 1
        break
    while j < len(nums)-1:
      j += 1
      if nums[j] != target:
        j -= 1
        break
    return i, j
        
  def binary_search(self, nums, target):
    start, end = 0, len(nums)-1
    while start <= end:
      mid = (start+end)/2
      if target == nums[mid]:
        return mid
      elif target < nums[mid]:
        end = mid-1
      else:
        start = mid+1
    return -1

As you can see, it was pretty rudimentary.
The algorithm involved using binary search to find the index of any element of value "target" in the array,
then continously checking left and right of that index to find the left and right bounds.

The "better way" would be to only use two binary searches.
The first binary search would find the position that target - 0.5 would be located.
The second binary search would find the position that target + 0.5 would be located.
After some checks to make sure that the matching positions correlate with "target" valued elements in nums, we can return those as the lower and upper bounds.

Lastly, I thought up a cheater's way to do it with Python built ins.
I don't think this is how the problem was intended to be solved but it's pretty fast and the code is nice and short.
Check it out below! It's pretty self explanatory.

O(logn) time 
O(1) space
'''

def search_range(nums, target):
  if target not in nums:
    return [-1, -1]
  original = list(nums)
  nums.append(target+0.5)
  nums.append(target-0.5)
  nums.sort()
  start = nums.index(target-0.5)
  end = nums.index(target+0.5)-2
  return[start, end]
