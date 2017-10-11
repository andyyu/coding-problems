# Andy Yu
'''
Find the contiguous subarray within an array (containing at least one number) which has the largest product.

For example, given the array [2,3,-2,4],
the contiguous subarray [2,3] has the largest product = 6.

--------------------------------------------------------------------------------

Difficulty: Medium

Solution notes:

O(n) time
O(1) space
'''

def max_product_subarray(nums):
    max_so_far = nums[0]
    neg_max = nums[0]
    pos_max = nums[0]
    for num in nums[1:]:
        if num < 0:
            neg_max, pos_max = min(pos_max*num, num), max(neg_max*num, num)
        else:
            neg_max = min(neg_max*num, num)
            pos_max = max(pos_max*num, num)
        max_so_far = max(max_so_far, pos_max)
    return max_so_far
