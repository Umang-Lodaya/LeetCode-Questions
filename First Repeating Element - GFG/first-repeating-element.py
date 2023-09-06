#User function Template for python3
from collections import Counter

class Solution:
    #Function to return the position of the first repeating element.
    def firstRepeated(self,arr, n):
        if not n:
            return -1
            
        else:
            a = Counter(arr)
            for item, count in enumerate(arr):
                if a[count] >= 2:
                    return item + 1
            
            return -1

#{ 
 # Driver Code Starts
#Initial Template for Python 3

#contributed by RavinderSinghPB
if __name__=='__main__':
    t=int(input())
    for _ in range(t):
        n=int(input())
        
        arr=[int(x) for x in input().strip().split()]
        ob = Solution()
        print(ob.firstRepeated(arr, n))
# } Driver Code Ends