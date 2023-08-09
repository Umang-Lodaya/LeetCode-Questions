#User function Template for python3

class Solution:
    def largestPrimeFactor (self, N):
        if N <= 1:
            return None
        
        result = None
        
        while N % 2 == 0:
            result = 2
            N //= 2
        
        d = 3
        while d * d <= N:
            while N % d == 0:
                result = d
                N //= d
            
            d += 2
        
        return N if N > 2 else result
        


#{ 
 # Driver Code Starts
#Initial Template for Python 3

if __name__ == '__main__': 
    t = int (input ())
    for _ in range (t):
        N = int(input())
       

        ob = Solution()
        print(ob.largestPrimeFactor(N))
# } Driver Code Ends