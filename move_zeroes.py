# Andy Yu
'''
Given an array nums, write a function to move all 0's to the end of it while maintaining the relative order of the non-zero elements.

For example, given nums = [0, 1, 0, 3, 12], after calling your function, nums should be [1, 3, 12, 0, 0].

Note:
You must do this in-place without making a copy of the array.
Minimize the total number of operations.

--------------------------------------------------------------------------------

Difficulty: Easy

Solution notes:

O(n) time
O(1) space
'''

def moveZeroes(nums):
    position = 0
    for i, num in enumerate(nums):
        if num != 0:
            nums[position], nums[i] = num, nums[position]
            position += 1
    return nums

if __name__ == "__main__":
    print(moveZeroes([0, 1, 0, 3, 12]))
