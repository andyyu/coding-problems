# Andy Yu
'''
You are given coins of different denominations and a total amount of money amount. 
Write a function to compute the fewest number of coins that you need to make up that amount. 
If that amount of money cannot be made up by any combination of the coins, return -1.

Example 1:
coins = [1, 2, 5], amount = 11
return 3 (11 = 5 + 5 + 1)

Note: You may assume you have an infinite number of each coin.

Difficulty: Medium

Solution notes:

- First iteration -
def compute_change(coins, amount):
  previous_results = {}

  # step through total amount, adding one more each time
  for i in xrange(amount + 1):
    # if the amount we're looking at is the value of any of the coins, set the result of that amount to 1
    if i in coins:
      previous_results[i] = 1
    
    # must be a sum of multiple coins
    else:
      # for every denomination of coin, subtract it from the total and see if we have a previous result for it
      for j in coins:
        if (i - j) in previous_results:
          previous_results[i] = previous_results[i - j] + 1

  return previous_results.get(amount, -1)

However, this solution is too slow (and also doesn't work for certain cases, can you figure out which?)

O(amount*coins) time
O(amount) space
Dynamic programming
'''

def coinChange(self, coins, amount):
  # intialize a list [0, MAX_INT, MAX_INT, ...]
  previous_results = [0] + [float('inf')]*amount
  # step through total amount
  for i in xrange(1, amount + 1):
      # list comprehension is MUCH faster, but the concept is the same as above solution - read the above if this doesn't make sense
      previous_results[i] = min([previous_results[i-c] if i >= c else float('inf') for c in coins]) + 1
  return -1 if previous_results[amount] == float('inf') else previous_results[amount]
        