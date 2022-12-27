class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        maxProfit = 0
        buyDate = 0
        sellDate = 1
        
        if len(prices) < 2:
            return 0
        
        while sellDate < len(prices):
            if prices[sellDate] < prices[buyDate]:
                buyDate = sellDate
            else:
                profit = prices[sellDate] - prices[buyDate]
                maxProfit = max(profit, maxProfit)
                
            sellDate += 1
                
        return maxProfit