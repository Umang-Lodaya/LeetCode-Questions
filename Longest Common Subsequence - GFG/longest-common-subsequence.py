#User function Template for python3

class Solution:
    
    #Function to find the length of longest common subsequence in two strings.
    def lcs(self, n, m, s1, s2):
        
        dp = [[-1 for j in range(m + 1)] for i in range(n + 1)]
    
        for i in range(n + 1):
            dp[i][0] = 0
    
        for i in range(m + 1):
            dp[0][i] = 0
    
        for ind1 in range(1, n + 1):
            for ind2 in range(1, m + 1):
                if s1[ind1 - 1] == s2[ind2 - 1]:
                    dp[ind1][ind2] = 1 + dp[ind1 - 1][ind2 - 1]
                else:
                    dp[ind1][ind2] = 0 + max(dp[ind1 - 1][ind2], dp[ind1][ind2 - 1])
        
        return dp[n][m]


#{ 
 # Driver Code Starts
#Initial Template for Python 3
import atexit
import io
import sys

# Contributed by : Nagendra Jha

if __name__ == '__main__':
    test_cases = int(input())
    for cases in range(test_cases):
        x,y = map(int,input().strip().split())
        s1 = str(input())
        s2 = str(input())
        ob=Solution()
        print(ob.lcs(x,y,s1,s2))
# } Driver Code Ends