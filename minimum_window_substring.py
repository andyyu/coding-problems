# Andy Yu
'''
Given a string S and a string T,
find the minimum window in S which will contain all the characters in T in complexity O(n).

Example:
---
S = 'abcde'
T = 'ace'

returns: 'abcde' from index 0 to 4
---
S = 'aaabbsdda'
T = 'ab'

returns: 'ab' from index 2 to 3
---
S = "ADOBECODEBANC"
T = "ABC"

returns: 'BANC' from index 9 to 12
---
S = "ab"
T = "b"

returns: 'b'
---
S = "aa"
T = "aa"

returns: 'aa'
--------------------------------------------------------------------------------

Difficulty: Medium-Hard

Solution notes:

For most substring problems we can use the following ideas:
    - invariant: a condition that we maintain to be true
    - use a hashmap to keep track of our invariant
    - use two pointers to explore our string and support our hashmap
    - have a way to store the best answer found so far

In this case, our two pointers should define the front index and end index of the window
(the substring that is being considered). We continue to move our two pointers
while maintaining the invariant - that the substring being considered contains all the characters in T and is thus a valid solution.

The hashmap we use can be the letters in T as the key, and the value can be the count of that character in T.
We should also store the shortest substring in S that we've found so far that maintains our invariant.

O(n) time
O(m) space
where n is the length of s, and m is the length of t.
'''
from collections import defaultdict

def min_window(s, t):
    start = 0
    best = (0, len(s)-1)
    required = defaultdict(int)
    need = len(t)
    if len(s) < len(t):
        return ""
    for c in t:
        required[c] += 1
    for end, c in enumerate(s):
        required[c] -= 1
        if required[c] >= 0:
            need -= 1
        while start < end and need == 0:
            if required[s[start]] >= 0:
                break
            required[s[start]] += 1
            if required[c] > 0:
                need += 1
            start += 1
        best = (start, end) if (need == 0 and end-start < best[1]-best[0]) else best
    if need == 0:
        return s[best[0]:best[1]+1]
    else:
        return ""


if __name__ == "__main__":
    print min_window("abcde", "ace")
