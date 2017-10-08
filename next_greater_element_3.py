# Andy Yu
'''
Given a positive 32-bit integer n, you need to find the smallest 32-bit integer which has exactly the same digits existing in the integer n and is greater in value than n.
If no such positive 32-bit integer exists, you need to return -1.

Example 1:
Input: 12
Output: 21

Example 2:
Input: 21
Output: -1

--------------------------------------------------------------------------------

Difficulty: Medium

Solution notes:

see bigger_is_greater

O(n) time
O(n) space
'''

def nextGreaterElement(n):
    num = [c for c in str(n)]
    length = len(num)
    last = num[-1]
    for i in xrange(length-1, -1, -1):
        digit = num[i]
        if digit >= last:
            last = digit
        else:
            replace = i
            while i < length-1 and num[i+1] > digit:
                i += 1
            num[replace], num[i] = num[i], num[replace]
            result = int(''.join(num[0:replace+1] + num[replace+1:length][::-1]))
            if result < (2**32)/2-1:
                return result
            else:
                break
    return -1

if __name__ == "__main__":
    print(nextGreaterElement(12443322))
