#User function Template for python3

class Solution:
    def checkDoorStatus(self, N):
        ans = []
        for number in range(1, N + 1):
            root = math.sqrt(number)
            if int(root + 0.5) ** 2 == number:
                ans.append(1)
            else:
                ans.append(0)
        
        return ans

#{ 
 # Driver Code Starts
#Initial Template for Python 3

import math
if __name__ == '__main__': 
    t = int (input ())
    for _ in range (t):
        N=int(input())
        
        ob = Solution()
        ptr = ob.checkDoorStatus(N)
        print(*ptr)
# } Driver Code Ends