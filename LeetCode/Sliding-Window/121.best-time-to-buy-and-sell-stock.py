class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        # conditions
        # buy a stock in single day -> sell a stock in future
        # what's the maximum profit?
        # return max profit from this transaction

        # so have to buy at minimum price and sell it at highset price in someday of future 
        # buy on lowest price one day  -> try to silumtate to sell every day, and pick the highest price
        # in order to do that, need try to simulate the lowest prices 

        # dive into code
        
        # min_price set as inf value so whichever comes first, it will store here
        min_price = float('inf')
        # max_profit for 0 to track of maximum profit
        max_profit = 0
        # curr_profit for 0 to compare with max_profit each time when iterate
        curr_profit = 0

        # will iterate prices to compare values
        for price in prices: 
            # lets update min price
            min_price = min(min_price, price)
            # then get a current profit 
            curr_profit = price - min_price 
            # update max_profit 
            max_profit = max(max_profit, curr_profit)
        
        return max_profit

# T: O(n)
# S: O(1)