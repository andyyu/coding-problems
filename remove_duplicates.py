# Andy Yu
'''
Given a sorted array, remove the duplicates in place such that each element appear only once and return the new length.

Do not allocate extra space for another array, you must do this in place with constant memory.

For example,
Given input array nums = [1,1,2],

Your function should return length = 2, with the first two elements of nums being 1 and 2 respectively. 
It doesn't matter what you leave beyond the new length.

Difficulty: Easy

Solution notes:
O(n) time
O(1) space

'''
class Solution(object):
    def removeDuplicates(self, nums):
        if not nums:
            return 0
        count = 1
        last = nums[0]
        for i, num in enumerate(nums):
            if num > last:
                self.swap(nums,i,count)
                last = num
                count += 1
        return count
                
    def swap(self, nums, i, j):
        temp = nums[i]
        nums[i] = nums[j]
        nums[j] = temp