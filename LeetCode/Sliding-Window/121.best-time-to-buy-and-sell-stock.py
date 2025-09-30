def maxProfit(prices):
    min_price = float('inf')
    max_profit = 0
    curr_profit = 0

    for price in prices:
        curr_profit = price - min_price
        max_profit = max(max_profit, curr_profit)

        min_price = min(price, min_price)

    return max_profit

# T: O(n)
# S: O(1)