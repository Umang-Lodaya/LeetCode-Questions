class Solution:
    def uniquePaths(self, m: int, n: int) -> int:
        prev, curr = [1]*n, [0]*n
        
        for i in range(1, m):
            curr[0] = prev[0]
            
            for j in range(1, n):
                curr[j] = prev[j] + curr[j-1]
            
            prev, curr = curr, [0]*n
        
        return prev[-1]