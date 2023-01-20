class Solution:
    def maxProfit(self,prices):
        buy = 0 
        sell = 1 
        
        profit = 0
        while sell < len(prices):
            currentProfit = prices[sell] - prices[buy]
            if prices[buy] < prices[sell]:
                profit = max(currentProfit, profit)
            else:
                buy = sell
            sell += 1
            
        return profit