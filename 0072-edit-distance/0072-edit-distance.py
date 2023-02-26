class Solution:
    def minDistance(self, word1: str, word2: str) -> int:
        l1 = len(word1)
        l2 = len(word2)
        
        dp=[[-1]*(l1+1) for i in range(l2+1)]
        
        for i in range(l1+1):
            dp[0][i] = i
        for i in range(l2+1):
            dp[i][0] = i

        for j in range(1, l2+1):
            for i in range(1, l1+1):
                if word1[i-1] == word2[j-1]:
                    dp[j][i] = dp[j-1][i-1]
                else:
                    insert = dp[j-1][i]
                    delete = dp[j][i-1]
                    replace = dp[j-1][i-1]
                    dp[j][i] = 1 + min(insert, delete, replace)

        return dp[l2][l1]