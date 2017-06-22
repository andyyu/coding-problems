# Andy Yu
'''
Given n pairs of parentheses, write a function to generate all combinations of well-formed parentheses.

For example, given n = 3, a solution set is:

"((()))", "(()())", "(())()", "()(())", "()()()"


Difficulty: Medium

Solution notes:

My first thought was to do this recursively.

def generateParenthesis(self, n):
  res = []
  if n == 1:
      res.append("()")
  else:
      self.generateHelper(n, res)
  return list(set(res))
                
def generateHelper(self, n, res, build=""):
  if n == 0:
      res.append(build)
  else:
      self.generateHelper(n-1, res, build+"()")
      self.generateHelper(n-1, res, "()"+build)
      self.generateHelper(n-1, res, "("+build+")")

This was the first iteration I made, but I ran into a clear problem: my code would never be able to generate
a combination like "(())(())", because I append an entire pair of parenthesis every time.
To fix this, it seemed to me that I would have to only append either the left or right parenthesis every recursive step.
The only problem with this is keeping the well-formedness. This was solved by adding the if check "if left < right"
on line 50 in this file. This ensures that a closing brace is added only if there are currently unclosed opening braces in the build. 

'''
def generateParenthesis(n):
  res = []
  generateHelper(res, n, n)
  return res
                
def generateHelper(res, left, right, build=""):
  if left == 0 and right == 0:
    res.append(build)
  else:
      if left > 0:
          generateHelper(res, left-1, right, build + "(")
      if left < right and right > 0:
          generateHelper(res, left, right-1, build + ")")

if __name__ == '__main__':
  print generateParenthesis(6)

