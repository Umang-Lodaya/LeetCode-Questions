#User function Template for python3
class Solution:
    def findLargest(self, N, S):
        # code here
        if S==0 and N==1:
            return 0
        if S==0 or 9*N<S:
            return -1
        op=9
        res=''
        for i in range(N):
            for j in range(9,-1,-1):
                if S>=j:
                    res+=str(j)
                    S-=j
                    break
        return res


#{ 
 # Driver Code Starts
#Initial Template for Python 3

if __name__ == '__main__':
    t = int(input())
    for _ in range(t):
        N, S = [int(x) for x in input().split()]
        
        ob = Solution()
        print(ob.findLargest(N, S))
# } Driver Code Ends