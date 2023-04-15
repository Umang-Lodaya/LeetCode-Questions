class Solution:
    def maxValueOfCoins(self, piles: List[List[int]], k: int) -> int:
        @functools.lru_cache(None)
        
        def dp(i,K):
            if k==0 or i==len(piles):
                return 0

            res, cur = dp(i + 1, K), 0
            for j in range(min(len(piles[i]), K)):
                cur += piles[i][j]
                res = max(res, cur + dp(i + 1, K - j - 1))

            return res

        return dp(0,k)