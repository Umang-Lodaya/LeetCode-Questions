class Solution:
    def maxProfit(self,prices):
        buy = 0 #Buy
        sell = 1 #Sell
        
        profit = 0
        while sell < len(prices):
            currentProfit = prices[sell] - prices[buy] #our current Profit
            if prices[buy] < prices[sell]:
                profit =max(currentProfit, profit)
            else:
                buy = sell
            sell += 1
            
        return profit