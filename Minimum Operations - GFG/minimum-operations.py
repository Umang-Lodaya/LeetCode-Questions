#User function Template for python3

class Solution:
    def minOperation(self, n):
        if n <= 3:
            return n
        
        if n % 2 == 0:
            return 1 + self.minOperation(n // 2)
        
        return 2 + self.minOperation(n // 2)


#{ 
 # Driver Code Starts
#Initial Template for Python 3

if __name__ == '__main__': 
    t = int(input())
    for _ in range(t):
        n = int(input())
        ob = Solution()
        print(ob.minOperation(n))
# } Driver Code Ends