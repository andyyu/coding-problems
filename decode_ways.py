# Andy Yu
'''
A message containing letters from A-Z is being encoded to numbers using the following mapping:

'A' -> 1
'B' -> 2
...
'Z' -> 26

Given an encoded message containing digits, determine the total number of ways to decode it.

For example,
Given encoded message "12", it could be decoded as "AB" (1 2) or "L" (12).

The number of ways decoding "12" is 2.

Difficulty: Medium

Solution notes:
Clearly a recurrence relation type problem. We can split the solution for a message of length n into two different outcomes.
If the last two characters in the string can be decoded separately (e.g. "...23" can be evaluated with "23" -> W or "2" -> B, "3" -> C),
then the number of ways that string can be decoded is num_decodings(n-1) + num_decodings(n-2).
The num_decodings(n-1) case is when we decode the last character separately, and the num_decodings(n-2) case is when we decode
the last two characters as a pair. Implementing this recurrence relation gives us this somewhat ugly code.

def num_decodings(s):
    if len(s) < 1 or s[0] == '0':
        return 0
    if len(s) == 1:
        if 27 > int(s) > 0:
            return len(s)
    elif len(s) > 1:
        if s[-1] == '0':
            if not (27 > int(s[-2:]) > 0):
                return 0
            else:
                if len(s) == 2:
                    return 1
                else:
                    return num_decodings(s[:-2])
        else:
            if 27 > int(s[-2:]) > 0 and s[-2] != '0':
                return max(1, num_decodings(s[:-2])) + num_decodings(s[:-1])
        return num_decodings(s[:-1])
    return 0

This works, but it's very slow. Why? Because there is a whole lot of duplicate computation going on. In our most common case,
we are returning num_decodings(s[:-2])) + num_decodings(s[:-1])). This could spawn up to 2^n separate computations! No good.

Thus, we turn to the wonder that is dynamic programming. We can cache the results we compute as we go, making the whole
process much faster.

O(n) time
O(n) space
dynamic programming
'''

def num_decodings(s):
    if len(s) == 0:     # empty string has 0 ways to decode
        return 0
    if s[0] == '0':     # if the first character is a 0, a proper decoding is impossible
        return 0
    store = [0]*len(s)  # initialize our dynamic programming store
    store[0] = 1        # since we already checked if the first character is 0, we already know the first character can be decoded
    for i in xrange(1, len(s)):     # iterate over the rest of the characters in the string and evaluate
        if s[i] == '0':             # if the new char is a 0, there are two possibilities
            if 27 > int(s[i-1:i+1]) > 0:    # this is the case where the character before (s[i-1]) allows the 0 to be decoded. (e.g. in "..20", when we encounter the 0 we are still able to decode because it can be decoded as "20")
                store[i] = (store[i-2] if i > 1 else 1)     # in this case, the two characters must be decoded as a pair ("20"), so # of ways = num_decodings(s-2) (e.g., num_decoding("...20") == num_decoding "...")
            elif s[i-1] == '0':             # this is the case where the character before does not allow the 0 to be decoded ("..00")
                return 0                                    # in this case, there is no decoding possible
        else:                       # if the new character is NOT a 0 there are again two possibilities
            if 27 > int(s[i-1:i+1]) > 0 and s[i-1] != '0':  # in this case, the new character + the previous character can be decoded separately, or as a pair
                store[i] = store[i-1] + (store[i-2] if i > 1 else 1)    # number of ways when decoded separately (store[i-1]) + as a pair (store[i-2])
            else:
                store[i] = store[i-1]                                   # the new char + previous char can only be decoded separately. (store[i-1])
    return store[-1]    # return the final count we stored, which is the total number of decodings possible

if __name__ == '__main__':
    print num_decodings("101")