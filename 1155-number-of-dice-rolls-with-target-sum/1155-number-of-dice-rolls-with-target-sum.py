class Solution:
    def numRollsToTarget(self, n: int, k: int, target: int) -> int:
        dp: List[List[int]] = [[0] * (n + 1) for _ in range(target + 1)]
        for i in range(1, k + 1):  # initialize first col
            if i <= target:
                dp[i][1] = 1
            else:
                break
                
        for j in range(2, n + 1):  # populate rest of dp matrix
            for i in range(j, target + 1):
                dp[i][j] = dp[i - 1][j - 1] + dp[i - 1][j] - dp[i - min(i - 1, k) - 1][j - 1]  # line *
        return dp[target][n] % (10**9 + 7)