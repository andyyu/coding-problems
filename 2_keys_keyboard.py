# Andy Yu
'''
Initially on a notepad only one character 'A' is present. You can perform two operations on this notepad for each step:

Copy All: You can copy all the characters present on the notepad (partial copy is not allowed).
Paste: You can paste the characters which are copied last time.

Given a number n.
You have to get exactly n 'A' on the notepad by performing the minimum number of steps permitted. Output the minimum number of steps to get n 'A'.

Example 1:
Input: 3
Output: 3
Explanation:
Intitally, we have one character 'A'.
In step 1, we use Copy All operation.
In step 2, we use Paste operation to get 'AA'.
In step 3, we use Paste operation to get 'AAA'.
Note:
The n will be in the range [1, 1000].

--------------------------------------------------------------------------------

Difficulty: Easy-Medium

Solution notes:
This is the dynamic programming solution.
There is a faster O(n) solution, but it's purely mathematics based and this is good practice for dp.

The crux of this solution is that given any number i of 'A's, if there is a divisible factor j,
then we can build i from j by copy pasting the string of j 'A's (i/j) times.
ex. If we are building 'AAAAAAAA' (8 'A's), we can see that 4 is a factor of 8.
We can thus build 'AAAAAAAA' by copying 'AAAA' (8/4 = 2) times.

We can improve our search of j by starting from i/2, since the largest possible factor of i is i/2.

O(n^2) time
O(n) space
'''

def minSteps(n):
    res = [0]*(n+1)
    for i in xrange(2, len(res)):
        res[i] = i
        for j in xrange(i/2, 2, -1):
            if i % j == 0:
                res[i] = min(res[j] + i/j, res[i])
    return res[n]
