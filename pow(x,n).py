# Andy Yu
'''
Implement pow(x, n).

Difficulty: Easy

Solution notes:
O(logn) time
O(1) space
'''

def my_pow(x, n):
  if n < 0:
    return self.myPow(1/x, -n)
  if n == 0:
    return 1
  if n == 2:
    return x*x
  if n % 2:
    return my_pow(x, n-1)*x
  else:
    return my_pow(my_pow(x, n/2), 2)