# Andy Yu
'''
Design an algorithm to find the maximum profit. You may complete as many transactions as you like (ie, buy one and sell one share of the stock multiple times) with the following restrictions:

You may not engage in multiple transactions at the same time (ie, you must sell the stock before you buy again).
After you sell your stock, you cannot buy stock on next day. (ie, cooldown 1 day)

Example:

prices = [1, 2, 3, 0, 2]

maxProfit = 3
transactions = [buy, sell, cooldown, buy, sell]

--------------------------------------------------------------------------------

Difficulty: Medium-Hard

Solution notes:
As with any DP problem, we should first identify which variables we should store as a memoized state.
Since there are 3 different actions possible on any given day (buy, sell, cooldown), we can create 3 arrays:

buy[n]
sell[n]
cooldown[n]

where buy[i] would equal the max profit when the last operation on or before day i was "buy". Our transition states would be:

buy[i] = max(cooldown[i-1]-price, buy[i-1])
sell[i] = max(buy[i-1]+price, sell[i-1])
cooldown[i] = max(sell[i-1], cooldown[i-1])

Since cooldown is the max of itself or sell, it can never be greater than sell. Thus, we can restructure our transition states to:

buy[i] = max(sell[i-2]-price, buy[i-1])
sell[i] = max(buy[i-1]+price, sell[i-1])

O(n) time
O(n) space
'''

def max_profit(prices):
    if len(prices) < 2:
        return 0
    buy = [-float('inf')]*len(prices)
    sell = [0]*len(prices)
    for i, price in enumerate(prices):
        if i < 2:
            buy[i] = max(-price, buy[i-1])
            if i == 1:
                sell[i] = max(buy[i-1]+price, sell[i-1])
            continue
        buy[i] = max(sell[i-2]-price, buy[i-1])
        sell[i] = max(buy[i-1]+price, sell[i-1])
    return sell[-1]
