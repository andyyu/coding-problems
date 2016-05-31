# Andy Yu
'''
Say you have an array for which the ith element is the price of a given stock on day i.

Design an algorithm to find the maximum profit. 
You may complete as many transactions as you like (ie, buy one and sell one share of the stock multiple times). 
However, you may not engage in multiple transactions at the same time (ie, you must sell the stock before you buy again).

Difficulty: Easy-Medium

Solution Notes:
At first glance this problem seems tricky.
However, realize the caveat that you may not engage in multiple transactions at the same time makes this problem very easy once you take it into account.
The pseudocode would be something like this:
Keep track of your bought price (lowest).
Keep track of the highest seen so far.
Iterate through all the prices. 
The only time we sell is when we find a price lower than the one before it.
Then we sell during the day before, and we buy again on the low day.

O(n) time
O(1) space
'''
def max_profit(prices):
  if len(prices) < 2:
    return 0
  lowest = prices[0]
  profit = 0
  for i in xrange(1, len(prices)):
    if prices[i] < prices[i-1]:
      profit += max(prices[i-1]-lowest, 0)
      lowest = prices[i]
  return profit + max(prices[i]-lowest, 0)
                
