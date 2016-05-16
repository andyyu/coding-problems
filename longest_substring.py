# Andy Yu
'''
Given a string, find the length of the longest substring without repeating characters.

Examples:

Given "abcabcbb", the answer is "abc", which the length is 3.

Given "bbbbb", the answer is "b", with the length of 1.

Given "pwwkew", the answer is "wke", with the length of 3. 
Note that the answer must be a substring, "pwke" is a subsequence and not a substring.

Difficulty: Medium

Solution notes:

For my solution I used a queue to keep track of the latest running substring.
I found a repeated letter, I would update the max_length found so far if it was bigger, 
then I would pop letters off the front of the substring until the first occurence of that letter was gone.

i.e.
input = "abcbe"
"a" -> "ab" -> "abc" -> "abcb" (found repeat)
check if length of current running substring is longest yet, and update max_length
then pop off the front until the first of the recurring letter (b) is gone
"abcb" -> "cb"
then continue
"cb" -> "cbe"

In hindsight, it would be faster to use a hashmap to keep track of previously encountered letters instead of a queue.

O(n) time
O(1) space
'''

def length_of_longest_substring(s):
  max_length = 0
  letter_queue = []
  for i in xrange(len(s)):
    if s[i] in letter_queue:
      max_length = max(max_length, len(letter_queue))
      while (letter_queue.pop(0) != s[i]):
        continue
    letter_queue.append(s[i])
  return max(max_length, len(letter_queue))