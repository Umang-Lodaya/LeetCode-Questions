#User function Template for python3

class Solution:
    def findK(self, a, n, m, k):
        left = 0; right = m - 1
        top = 0; bottom = n - 1
        
        while left <= right and top <= bottom:
            for j in range(left, right + 1):
                k -= 1
                if k == 0:
                    return a[top][j]
            
            top += 1
            
            for i in range(top, bottom + 1):
                k -= 1
                if k == 0:
                    return a[i][right]
            
            right -= 1
            
            for j in range(right, left - 1, -1):
                k -= 1
                if k == 0:
                    return a[bottom][j]
            
            bottom -= 1
            
            for i in range(bottom, top - 1, -1):
                k -= 1
                if k == 0:
                    return a[i][left]
                    
            left += 1
        
#{ 
 # Driver Code Starts

#Initial Template for Python 3

for _ in range(int(input())):
    n, m, k = map(int,input().split())
    a = [
            list(map(int,input().split()))
            for _ in range(n)
        ]
    
    ob = Solution()
    print(ob.findK(a,n,m,k))
    
# } Driver Code Ends