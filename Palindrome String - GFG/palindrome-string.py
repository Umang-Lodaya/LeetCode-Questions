#User function Template for python3
class Solution:
	def isPalindrome(self, S):
	   n = len(S)
	   if n == 1: return 1
	    
	   for i in range(n // 2):
	       if S[i] != S[n - 1 - i]:
	           return 0
	   
	   return 1


#{ 
 # Driver Code Starts
#Initial Template for Python 3

if __name__ == '__main__':
	T=int(input())
	for i in range(T):
		S = input()
		ob = Solution()
		answer = ob.isPalindrome(S)
		print(answer)

# } Driver Code Ends