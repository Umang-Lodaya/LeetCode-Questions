#User function Template for python3

from typing import List
from queue import Queue
class Solution:
    #Function to return Breadth First Traversal of given graph.
    def bfsOfGraph(self, V: int, adj: List[List[int]]) -> List[int]:
        OPEN = [0]
        CLOSED = []
        
        while OPEN:
            node = OPEN.pop(0)
            childern = adj[node]
            for child in childern:
                if child not in OPEN:
                    if child not in CLOSED:
                        OPEN.append(child)
            
            CLOSED.append(node)
        
        return CLOSED
        # code here


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