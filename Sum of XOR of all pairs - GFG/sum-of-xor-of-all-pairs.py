#User function Template for python3
class Solution:
    def sumXOR (self, arr, n): 
        ans = 0; bit = 1
        maxbin = len(bin(max(arr))) - 2 
        
        for i in range(maxbin + 1):
            count = 0
            for j in range(n):
                if arr[j] & (bit):
                    count += 1
                    
            ans += (bit) * count * (n - count)
            bit = bit << 1
            
        return ans



#{ 
 # Driver Code Starts
#Initial Template for Python 3



for _ in range(0,int(input())):
    
    n = int(input())
    arr = list(map(int,input().strip().split()))
    ob = Solution()
    res = ob.sumXOR(arr, n)
    print(res)


# } Driver Code Ends