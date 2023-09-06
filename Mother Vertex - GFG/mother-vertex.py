
class Solution:
    def dfs(self, adj, i, visited):
        visited[i] = True
        for v in adj[i]:
            if not visited[v]:
                self.dfs(adj, v, visited)
    
	def findMotherVertex(self, V, adj):
		visited = [False for i in range(V)]
		res = -1
		for i in range(V):
		    if not visited[i]:
		        self.dfs(adj, i, visited)
		        res = i
		
		visited = [False for i in range(V)]
		self.dfs(adj, res, visited)
		
		if all(visited):
		    return res
		   
		return -1


#{ 
 # Driver Code Starts
#Initial Template for Python 3

import sys 

sys.setrecursionlimit(10**6) 
if __name__ == '__main__':
	T=int(input())
	for i in range(T):
		V, E = map(int, input().split())
		adj = [[] for i in range(V)]
		for _ in range(E):
			u, v = map(int, input().split())
			adj[u].append(v)
		obj = Solution()
		ans = obj.findMotherVertex(V, adj)
		print(ans)
# } Driver Code Ends