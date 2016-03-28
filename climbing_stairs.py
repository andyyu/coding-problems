# Andy Yu
'''
You are climbing a stair case. It takes n steps to reach to the top.

Each time you can either climb 1 or 2 steps. In how many distinct ways can you climb to the top?
Difficulty: Easy

Solution notes:
basically Fibonacci, so a naive implentation would look something like

def ways_to_climb(n):
  if n <= 1:
    return 1
  else:
    return ways_to_climb(n-1) + ways_to_climb(n-2)

but recursion is slow. We could use the Fibonacci formula and get O(1) time/space complexity, but that seems a bit unfair.
One faster way to implement this is using memoization - which is basically storing the results of expensive function calls and returning the cached result when the same inputs occur again.

def ways_to_climb(n):
  store = [-1]*(n+1)
  store[0] = 1
  store[1] = 1
  for i in xrange(n+1):
    store[i] = store[i-1] + store[i-2]
  return store[n]

this is much faster than our 2^n recursive implementation, but it requires O(n) space.
What if we only cached what we needed?

-code shown below-

This is slightly slower, but only requires O(1) space.

O(n) time
O(1) space
dynamic programming
'''

def ways_to_climb(n):
  if n == 1:
      return 1
  a, b = 1, 2
  for i in xrange(2, n):
      temp = b
      b = a+b
      a = temp
  return b