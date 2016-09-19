# Andy Yu
'''
Given an integer n, return 1 - n in lexicographical order.

For example, given 13, return: [1,10,11,12,13,2,3,4,5,6,7,8,9].

Please optimize your algorithm to use less time and space. The input size may be as large as 5,000,000.


Difficult: Medium

Solution Notes:
Version using sort() and string / int conversion. Simple but slow (took 95 ms average for n=10000).

def lexical_order(n):
  result = [str(i+1) for i in xrange(n)]
  result.sort()
  return [int(i) for i in result]


Next iteration. Went for DFS - but the code is clumsy and inelegant. Still got a decent speedup so this is the right track (took 83 ms average for n=10000).

def lexicalOrder(self, n):
  results = []
  front = [str(i) for i in xrange(1, 10)]
  cons = [str(i) for i in xrange(-1, 10)]
  length = len(str(n))
  self.dfs(front, cons, "", 0, length, n, results)
  return results
    
def dfs(self, front, cons, path, index, length, n, results):
  if index < length:
    if index == 0:
      possible_digits = front
    else:
      possible_digits = cons
    for j in possible_digits:
      if j != "-1":
        next_int = path + j
        if int(next_int) > n:
          break
        results.append(int(next_int))
        self.dfs(front, cons, next_int, index+1, length, n, results)


Finally, the refactored version of my DFS idea - but, it was still too slow to pass leetcode's test! (Again, took 83 ms average for n=10000).

def lexicalOrder(self, n):
  results = []
  for i in xrange(1, 10):
    self.dfs(i, n, results)
  return results
  
def dfs(self, num, n, results):
  if num <= n:
    results.append(num)
    num *= 10
    for i in xrange(10):
      self.dfs(num+i, n, results)

So, I ended up adding one last improvement that would reduce the number of dfs() calls

O(n) time
O(n) space
'''
def lexical_order(n):
  results = []
  for i in xrange(1, 10):
    self.dfs(i, n, results)
  return results
  
def dfs(self, num, n, results):
  if num <= n:
    results.append(num)
    num *= 10
    if num <= n:              # speedup: before, prevents dfs() being called 10 times even when each wouldn't get past the initial num<=n check
      for i in xrange(10):
        self.dfs(num+i, n, results)
  

