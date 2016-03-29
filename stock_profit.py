# Andy Yu
'''
Suppose we could access yesterday's Apple stock prices as a list, where:

The indices are the time in minutes past trade opening time, which was 9:30am local time.
The values are the price in dollars of Apple stock at that time.
So if the stock cost $500 at 10:30am, stock_prices_yesterday[60] = 500.

Write an efficient function that takes stock_prices_yesterday and returns the best profit I could have made from 1 purchase and 1 sale of 1 Apple stock yesterday.
Difficulty: Medium

Solution notes:
O(n) time
O(1) space
dynamic programming

'''
def get_max_profit(stock_prices):
  # must be at least 2 stock prices or no profit possible
  if len(stock_prices) < 2:
      return 0

  # keep track of the lowest stock price so far, so we can use it to find the biggest profit we can get
  # from selling at any point in time.
  min_price = stock_prices[0]
  
  # largest profit seen so far
  max_profit = stock_prices[1] - stock_prices[0]

  for time, current_price in enumerate(stock_prices):
      # must buy a stock first, so we can't possibly sell at time 0
      if time == 0:
          continue

      # get biggest profit if we had purchased at the lowest price seen so far and sold now
      potential_profit = current_price - min_price
 
      max_profit = max(max_profit, potential_profit)
      min_price  = min(min_price, current_price)

  return max_profit

