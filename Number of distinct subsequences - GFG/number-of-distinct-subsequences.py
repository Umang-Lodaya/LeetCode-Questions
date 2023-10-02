#User function Template for python3

class Solution:
    def distinctSubsequences(self, S):
        n = len(S)
        MOD = 10**9 + 7
        arr = [0 for _ in range(26)]
        pre = 1; cur = 1
        for i in range(n):
            cur = (pre * 2) % MOD
            cur = (cur - arr[ord(S[i]) - ord('a')] + MOD) % MOD
            arr[ord(S[i]) - ord('a')] = pre
            pre = cur
        
        return cur


#{ 
 # Driver Code Starts
#Initial Template for Python 3

if __name__ == '__main__':
	T=int(input())
	for i in range(T):
		s = input()

		ob = Solution()
		answer = ob.distinctSubsequences(s)
		print(answer)

# } Driver Code Ends