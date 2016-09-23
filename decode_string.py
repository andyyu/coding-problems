# Andy Yu
'''
Given an encoded string, return it's decoded string.

The encoding rule is: k[encoded_string], where the encoded_string inside the square brackets is being repeated exactly k times. Note that k is guaranteed to be a positive integer.

You may assume that the input string is always valid; No extra white spaces, square brackets are well-formed, etc.

Furthermore, you may assume that the original data does not contain any digits and that digits are only for those repeat numbers, k. For example, there won't be input like 3a or 2[4].

Examples:

s = "3[a]2[bc]", return "aaabcbc".
s = "3[a2[c]]", return "accaccacc".
s = "2[abc]3[cd]ef", return "abcabccdcdcdef".

Difficult: Medium

Solution Notes:

My first attempt was to do it iteratively. Unfortunately, I soon realized there were way too many edge cases to make an elegant solution.
(still works though!)

class Solution(object):
    def decodeString(self, s):
        return self.decodeStringHelper(1, s)
        
    def decodeStringHelper(self, k, s):
        count = 0
        multiple = 1
        start = 0
        end = 0
        start_string = ""
        while s and not s[0].isdigit():
            start_string+=s[0]
            s=s[1:]
        if not s:
            return k*start_string
        for i in xrange(len(s)):
            if s[i] == "[": 
                if count == 0: # first "["
                    start = i+1
                    multiple = int(s[:i])
                count += 1
            if s[i] == "]":
                count -= 1
                if count == 0:
                    end = i
                    break
        capture = s[start:end]
        return k*(start_string + self.decodeStringHelper(multiple, s[start:end]) + self.decodeStringHelper(1, s[end+1:]))
        
I decided to adjust my approach and go for a stack instead, which I thought would handle all the variations better than a recursive approach.


'''
class Solution(object):
  def decodeString(self, s):
    stack = [[1, ""]]
    num = ""
    for c in s:
      if c.isdigit():
        num += c
      elif c == "[":
        stack.append([int(num), ""])
        num = ""
      elif c == "]":
        bound = stack.pop()
        stack[-1][1] += (bound[0]*bound[1])
      else:
        stack[-1][1] += c
    return stack[-1][1]

