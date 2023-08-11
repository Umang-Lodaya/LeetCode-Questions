class Solution:
    def change(self, amount: int, coins: List[int]) -> int:
        dp = [[0 for j in range(amount+1)] for i in range(len(coins))]
        
        for j in range(amount + 1):
            if j % coins[0] == 0:
                dp[0][j] = 1
        
        for i in range(1, len(coins)):
            for j in range(amount + 1):
        
                notTake = dp[i-1][j]
                take = 0
                if amount >= coins[i]:
                    take = dp[i][j - coins[i]]

                dp[i][j] =  notTake + take
        
        return dp[len(coins) - 1][amount]