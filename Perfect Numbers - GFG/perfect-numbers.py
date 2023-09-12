#User function Template for python3

class Solution:
    def isPerfectNumber(self, N):
        if N == 1: return 0
        s = 0
        i = 2
        while i * i <= N:
            if N % i == 0:
                s += i
                if i != N // i:
                    s += N // i
            i += 1
            
        s += 1
        return 1 if s == N else 0


#{ 
 # Driver Code Starts
#Initial Template for Python 3

if __name__ == '__main__': 
    t = int (input ())
    for _ in range (t):
        N=int(input())
        
        ob = Solution()
        print(ob.isPerfectNumber(N))
# } Driver Code Ends