# Andy Yu
'''
Find all possible combinations of k numbers that add up to a number n,
given that only numbers from 1 to 9 can be used and each combination should be a unique set of numbers.


Example 1:
Input: k = 3, n = 7
Output:
[[1,2,4]]

Example 2:
Input: k = 3, n = 9
Output:
[[1,2,6], [1,3,5], [2,3,4]]

Difficulty: Medium

Solution notes:
Use recursion, note that since we don't want duplicates (unique set of numbers), we can always build 1->9.
Use "last" to keep track of the last number added (and only further add numbers larger than that).
    - we could also just check the last element of the list manually
Make sure to pass in "nums + [i]" to your recursive call to create a -new- list.
Appending i to nums will pass the same list object around, making the storing of previous solutions impossible.
'''

def combination_sum_3(k, n):
    res = []
    combination_sum_helper(k, n, [], 0, res)
    return res

def combination_sum_helper(k, n, nums, last, res):
    curr_sum = sum(nums)
    length = len(nums)
    if k == 0:
        if curr_sum == n:
            res.append(nums)
        return
    for i in xrange(last+1, 10):
        if curr_sum + i <= n:
            combination_sum_helper(k-1, n, nums + [i], i, res)

if __name__ == "__main__":
    print combination_sum_3(3, 9)
