#User function Template for python3
class Solution:
    def searchWord(self, arr, s):
        m, n = len(arr), len(arr[0])
        
        ans = []
        dir = [[-1, 0], [0, -1], [0, 1], [1, 0], [-1, -1], [1, 1], [-1, 1], [1, -1]]
        
        def solve(i, j, arr, s, m, n, k):
            it = 0
            
            while i>=0 and i<m and j>=0 and j<n and it < len(s):
                if arr[i][j] != s[it]:
                    return False
                
                it += 1
                i += dir[k][0]
                j += dir[k][1]
           
            return it == len(s)      
        
        for i in range(m):
            for j in range(n):
                curr = False
                for k in range(8):
                    curr |= solve(i, j, arr, s, m, n, k)
                
                if curr:
                    ans.append([i, j])
        
        return ans


#{ 
 # Driver Code Starts
#Initial Template for Python 3

if __name__ == '__main__':
	T=int(input())
	for i in range(T):
		n, m = input().split()
		n = int(n); m = int(m);
		grid = []
		for _ in range(n):
			cur  = input()
			temp = []
			for __ in cur:
				temp.append(__)
			grid.append(temp)
		word = input()
		obj = Solution()
		ans = obj.searchWord(grid, word)
		for _ in ans:
			for __ in _:
				print(__, end = " ")
			print()
		if len(ans)==0:
		    print(-1)

# } Driver Code Ends