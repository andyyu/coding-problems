# Andy Yu
'''
Given m arrays, and each array is sorted in ascending order. Now you can pick up
two integers from two different arrays (each array picks one) and calculate the
distance. We define the distance between two integers a and b to be their
absolute difference |a-b|. Your task is to find the maximum distance.

Input:
[[1,2,3],
 [4,5],
 [1,2,3]]
Output: 4
Explanation:
One way to reach the maximum distance 4 is to pick 1 in the first or third array
and pick 5 in the second array.

Note:
Each given array will have at least 1 number. There will be at least two non-empty arrays.
The total number of the integers in all the m arrays will be in the range of [2, 10000].
The integers in the m arrays will be in the range of [-10000, 10000].

--------------------------------------------------------------------------------

Difficulty: Easy

Solution notes:

We know the biggest absolute difference |a-b| will occur when a is the biggest
number and b is the smallest number. However, a and b must be from different
arrays. Since the arrays are conveniently sorted in ascending order, we can
simply find the array (1) with the smallest minimum value, and find a different
array (2) that has the largest maximum value.
To make sure we aren't missing any better combination by assuming (1) contributes
the minimum value, we also need to check if the largest absolute difference
found using (1)'s max value as a will produce a better result.

O(n) time
O(1) space
'''

def maxDistance(arrays):
    """
    :type arrays: List[List[int]]
    :rtype: int
    """
    max_val, max_index = max([(array[-1], i) for i, array in enumerate(arrays)])
    min_val, min_index = min([(array[0], i) for i, array in enumerate(arrays)])
    max_a = max([max_val - arrays[i][0] for i in xrange(len(arrays)) if i != max_index])
    max_b = max([arrays[i][-1] - min_val for i in xrange(len(arrays)) if i != min_index])
    return max(max_a, max_b)
