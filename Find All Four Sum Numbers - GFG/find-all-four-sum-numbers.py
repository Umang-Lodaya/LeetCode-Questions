#User function Template for python3

# arr[] : int input array of integers
# k : the quadruple sum required

class Solution:
    def fourSum(self, arr, k):
        arr.sort()
        n = len(arr)
        res = []
        for i in range(n - 3):
            if i > 0 and arr[i] == arr[i - 1]:
                continue
            
            for j in range(i + 1, n - 2):
                if j > i + 1 and arr[j] == arr[j - 1]:
                    continue
                
                l = j + 1
                r = n - 1
                while l < r:
                    if arr[i] + arr[j] + arr[l] + arr[r] == k:
                        res.append([arr[i], arr[j], arr[l], arr[r]])
                        while l < r and arr[l] == arr[l + 1]:
                            l += 1
                        l += 1
                        
                        while l < r and arr[r] == arr[r - 1]:
                            r -= 1
                        r -= 1
                    
                    elif arr[i] + arr[j] + arr[l] + arr[r] < k:
                        l += 1
                    
                    else:
                        r -= 1
                        
        return sorted(res)
        


#{ 
 # Driver Code Starts
#Initial Template for Python 3


#Main
if __name__=='__main__':
    t = int(input())
    while t:
        t-=1
        n, k=map(int,input().split())
        # print(n, k)
        a=list(map(int,input().strip().split()))[:n]
        # print(a)
        ob=Solution()
        ans=ob.fourSum(a, k)
        # print(ans)
        for v in ans:
            for u in v:
                print(u, end=" ")
            print("$", end="")
        if(len(ans)==0):
            print(-1, end="")
        print()
        
        

# } Driver Code Ends