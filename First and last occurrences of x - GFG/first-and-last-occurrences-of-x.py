#User function Template for python3


class Solution:
    def getIndex(self, arr, n, x, isFirst = True):
        l = 0; h = n - 1
        ans = -1
        while l <= h:
            mid = l + (h - l) // 2
            if arr[mid] == x:
                ans = mid
                if isFirst:
                   h = mid - 1
                else:
                    l = mid + 1
                    
            elif arr[mid] < x:
                l = mid + 1
            else:
                h = mid - 1
                
        return ans
    
    def find(self, arr, n, x):
        f = self.getIndex(arr, n, x, isFirst = True)
        if f == -1:
            return [-1, -1]
            
        l = self.getIndex(arr, n, x, isFirst = False)
        return [f, l]
        


#{ 
 # Driver Code Starts
t=int(input())
for _ in range(0,t):
    l=list(map(int,input().split()))
    n=l[0]
    x=l[1]
    arr=list(map(int,input().split()))
    ob = Solution()
    ans=ob.find(arr,n,x)
    print(*ans)
# } Driver Code Ends