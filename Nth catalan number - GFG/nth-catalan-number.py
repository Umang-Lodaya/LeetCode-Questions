
class Solution:
    def findCatalan(self, n : int) -> int:
        # code here
        
        MOD = 10 ** 9 + 7
        
        def solve():
            dp = [-1 for i in range(n + 1)]
            
            for i in range(n + 1):
                if i == 0 or i == 1:
                    dp[i] = 1
                    
                else:
                    curr = 0
                    for j in range(0, i//2):
                        s1 = dp[j] % (MOD)
                        s2 = dp[i - 1 - j] % (MOD)
                        curr = (curr + s1 * s2) % (MOD)
                    
                    dp[i] = 2 * curr
                    
                    if i % 2:
                        dp[i] += dp[i//2] ** 2 
                    
                    dp[i] = dp[i] % (MOD)
            
            return dp[n]
            
        return solve() % MOD


#{ 
 # Driver Code Starts
if __name__=="__main__":
    t = int(input())
    for _ in range(t):
        
        n = int(input())
        
        obj = Solution()
        res = obj.findCatalan(n)
        
        print(res)
        

# } Driver Code Ends