#User function Template for python3

class Solution:
	def singleNumber(self, nums):
		xor = 0
		for i in nums:
		    xor ^= i
		
		n1 = 0; n2 = 0
		k = xor & ~(xor - 1)
		for i in nums:
		    if i & k != 0:
		        n1 ^= i
		    else:
		        n2 ^= i
		
		if n1 > n2:
		    return [n2, n1]
		    
		return [n1, n2]



#{ 
 # Driver Code Starts
#Initial Template for Python 3

if __name__ == '__main__':
	T=int(input())
	for i in range(T):
		n = int(input())
		v = list(map(int,input().split()))
		ob = Solution();
		ans = ob.singleNumber(v)
		for i in ans:
			print(i, end = " ")
		print()

# } Driver Code Ends