#User function Template for python3

from typing import List
from queue import Queue

class Solution:
    def bfsOfGraph(self, V: int, adj: List[List[int]]) -> List[int]:
        if V == 1:
            return [0]
        
        queue = [0]
        visited = [False for _ in range(V)]
        visited[0] = True
        path = []
        while queue:
            u = queue.pop(0)
            for v in adj[u]:
                if not visited[v]:
                    visited[v] = True
                    queue.append(v)
            
            path.append(u)
        
        return path


#{ 
 # Driver Code Starts


if __name__ == '__main__':
	T=int(input())
	for i in range(T):
		V, E = map(int, input().split())
		adj = [[] for i in range(V)]
		for _ in range(E):
			u, v = map(int, input().split())
			adj[u].append(v)
		ob = Solution()
		ans = ob.bfsOfGraph(V, adj)
		for i in range(len(ans)):
		    print(ans[i], end = " ")
		print()
        

# } Driver Code Ends