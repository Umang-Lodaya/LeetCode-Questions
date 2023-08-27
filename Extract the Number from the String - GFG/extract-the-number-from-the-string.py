import re

class Solution:
    def ExtractNumber(self, S):
        ans = re.findall('\d+', S)
        if not ans:
            return -1
            
        ans = list(map(int, ans))
        ans.sort()
        
        for i in range(len(ans) - 1, -1, -1):
            if '9' not in str(ans[i]):
                return ans[i]
        
        return -1

#{ 
 # Driver Code Starts

t=int(input())
for _ in range(t):
    S=input()
    ob=Solution()
    ans=ob.ExtractNumber(S)
    print(ans)   
# } Driver Code Ends