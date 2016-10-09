# Andy Yu
'''
https://leetcode.com/problems/partition-equal-subset-sum/

Given a non-empty array containing only positive integers, find if the array can be partitioned into two subsets such that the sum of elements in both subsets is equal.

Note:
Both the array size and each of the array element will not exceed 100.

Example 1:

Input: [1, 5, 11, 5]

Output: true

Explanation: The array can be partitioned as [1, 5, 5] and [11].
Example 2:

Input: [1, 2, 3, 5]

Output: false

Explanation: The array cannot be partitioned into equal sum subsets.

Difficulty: Easy

Solution notes:
We can immediately rule out sets that are not divisible by 2. If their sum is odd, then they clearly won't be able to be split into equal subsets.
Next, we can boil this problem down further. If both subsets are equal, then we can deduce that the sum of one subset will equal half of the sum of the entire set.
Thus, the problem is reduced to the subset sum problem - finding a subset that adds up to a value (in our case, sum(set)/2).
Unfortunately, this problem is also NP complete... meaning its complexity is of nondeterministic polynomial time.
In the worst case scenario, this would result in 2^n complexity (having to check every single combination).
In this problem I used a fairly common subset sum solution, but there IS a DP solution that can produce better results.
However, it's fairly complicated and better left for a different problem (check subset_sum.py).

O(2^n) time
O(1) space
'''

class Solution(object):
    def canPartition(self, nums):
        s = sum(nums)
        if s % 2 == 0:
            partition_value = s/2
            return self.findSubsetSum(nums, partition_value)
        return False
            
    def findSubsetSum(self, nums, s, path=[]):
        if s == 0:
            return True
        if s < 0:
            return False
        for i, num in enumerate(nums):
            new_list = list(nums)
            new_list.pop(i)
            return self.findSubsetSum(new_list, s-num, path+[num]) or self.findSubsetSum(new_list, s, path)
        return False

