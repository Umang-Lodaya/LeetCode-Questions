#User function Template for python3
class Solution:
	def equilibrium(self, arr, n): 
    	pre = [0 for i in range(n)]
    	suf = [0 for i in range(n)]
    	
    	p = 0; s = 0
    	for i in range(n):
    	    p += arr[i]
    	    pre[i] = p
    	
    	for i in range(n-1, -1, -1):
    	    s += arr[i]
    	    suf[i] = s
    	
    	ans = False
    	for i in range(n):
    	    if pre[i] == suf[i]:
    	        ans = True
    	        break
    	
    	if ans:
    	    return 'YES'
    	else:
    	    return 'NO'
    	


#{ 
 # Driver Code Starts
#Initial Template for Python 3

if __name__ == '__main__': 

	
	tc=int(input())
	while tc > 0:
	    n=int(input())
	    a=list(map(int , input().strip().split()))
	    ob = Solution()
	    ans=ob.equilibrium(a, n)
	    print(ans)
	    tc=tc-1
# } Driver Code Ends