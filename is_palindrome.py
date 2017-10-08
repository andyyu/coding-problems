# Andy Yu
'''
Given a string, determine if it is a palindrome, considering only alphanumeric characters and ignoring cases.

For example,
"A man, a plan, a canal: Panama" is a palindrome.
"race a car" is not a palindrome.

Note:
Have you consider that the string might be empty? This is a good question to ask during an interview.

For the purpose of this problem, we define empty string as valid palindrome.

--------------------------------------------------------------------------------

Difficulty: Easy

Solution notes:

O(n) time
O(1) space
'''

def isPalindrome(s):
       return ''.join(c for c in s.lower() if c.isalnum()) == ''.join(c for c in s[::-1].lower() if c.isalnum())
