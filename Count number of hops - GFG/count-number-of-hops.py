#User function Template for python3

class Solution:
    #Function to count the number of ways in which frog can reach the top.
    def countWays(self, n):
        MOD = 1000000007
        dp = [-1 for i in range(n+1)]
        
        def dfs(n):
            nonlocal dp
            if n <= 3:
                return 1 << n-1
                
            if dp[n] == -1:
                dp[n] = (dfs(n-1) + dfs(n-2) + dfs(n-3)) % MOD
            
            return dp[n]
        
        return dfs(n)


#{ 
 # Driver Code Starts
#Initial Template for Python 3
import atexit
import io
import sys
sys.setrecursionlimit(10**6)
# Contributed by : Nagendra Jha

if __name__ == '__main__':
    test_cases = int(input())
    for cases in range(test_cases):
        m = int(input())
        ob=Solution()
        print(ob.countWays(m))
# } Driver Code Ends