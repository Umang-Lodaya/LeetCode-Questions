class Solution:
    def ways(self, amount, coins, i, dp):
        if i == 0:
            return 1 if amount % coins[0] == 0 else 0
        
        if dp[i][amount] != -1:
            return dp[i][amount]
        
        notTake = self.ways(amount, coins, i-1, dp)
        take = 0
        if amount >= coins[i]:
            take = self.ways(amount - coins[i], coins, i, dp)
        
        dp[i][amount] =  notTake + take
        return dp[i][amount]
    
    def change(self, amount: int, coins: List[int]) -> int:
        dp = [[-1 for j in range(amount+1)] for i in range(len(coins))]
        return self.ways(amount, coins, len(coins) - 1, dp)