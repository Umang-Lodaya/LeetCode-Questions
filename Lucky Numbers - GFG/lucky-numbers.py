#User function Template for python3

class Solution:
    def isL(self, n, i):
        if n < i: return True
        if n % i == 0: return False
        return self.isL(n - n // i, i + 1)
        
    def isLucky(self, n): 
        return self.isL(n, 2)
        #RETURN True OR False


#{ 
 # Driver Code Starts
#Initial Template for Python 3

#contributed by RavinderSinghPB

if __name__ == '__main__':
    t=int(input())
    
    for tcs in range(t):
        n=int(input())
        obj = Solution()
        if obj.isLucky(n):
            print(1)
        else:
            print(0)
        
# } Driver Code Ends