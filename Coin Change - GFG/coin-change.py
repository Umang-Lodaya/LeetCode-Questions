#User function Template for python3

class Solution:
    def count(self, coins, N, Sum):
        dp = [[0 for j in range(Sum + 1)] for i in range(N)]
        
        for j in range(Sum + 1):
            if j % coins[0] == 0:
                dp[0][j] = 1
        
        for i in range(1, N):
            for j in range(Sum + 1):
                NT = dp[i-1][j]
                T = 0
                if j >= coins[i]:
                    T = dp[i][j - coins[i]]
                
                dp[i][j] = NT + T
        
        return dp[N - 1][Sum]



#{ 
 # Driver Code Starts
#Initial Template for Python 3

import sys
sys.setrecursionlimit(10**6)

if __name__ == '__main__': 
    t = int(input())
    for _ in range(t):
        sum,N = list(map(int, input().strip().split()))
        coins = list(map(int, input().strip().split()))
        ob = Solution()
        print(ob.count(coins,N,sum))

# } Driver Code Ends