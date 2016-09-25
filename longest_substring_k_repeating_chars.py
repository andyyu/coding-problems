# Andy Yu
'''
Find the length of the longest substring T of a given string (consists of lowercase letters only) such that every character in T appears no less than k times.

Example 1:

Input:
s = "aaabb", k = 3

Output:
3

The longest substring is "aaa", as 'a' is repeated 3 times.
Example 2:

Input:
s = "ababbc", k = 2

Output:
5

The longest substring is "ababb", as 'a' is repeated 2 times and 'b' is repeated 3 times.

Difficult: Medium - Hard

Solution Notes:
The trick I used to design an algorithm for this problem was the idea that the longest substring can never contain a letter that does appear at least k times in the entire string.
Running off of this idea, my solution first finds the least frequent character under k, and splits the string using that character, then recursively calls the find longest substring function on the split substrings.

'''
def longestSubstring(self, s, k):
  if not s:
    return 0
  least_char = min(set(s), key = s.count) # get least frequent character
  if s.count(least_char) < k:  # if the count of the least frequent char is less than k, then iterate over substrings created by splitting s by char
    return max(self.longestSubstring(substr, k) for substr in s.split(least_char)) 
  else:                        # else the string contains all characters of k repeating chars
    return len(s)
