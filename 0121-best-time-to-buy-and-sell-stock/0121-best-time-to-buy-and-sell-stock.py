class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        curr = 0
        maxp = 0
        minp = prices[0]
        n = len(prices)
        
        for i in range(1, n):
            curr = prices[i] - minp
            maxp = max(curr, maxp)
            minp = min(prices[i], minp)

        return maxp