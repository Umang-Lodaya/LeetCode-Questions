#User function Template for python3

class Solution:
    
    #Function to return a list containing the DFS traversal of the graph.
    def dfsOfGraph(self, V, adj):
        if V == 1:
            return [0]
        
        visited = [False for _ in range(V)]
        visited[0] = True
        path = []
        
        def dfs(node):
            nonlocal path
            visited[node] = True
            path.append(node)
            for v in adj[node]:
                if not visited[v]:
                    dfs(v)
        
        dfs(0)
        
        return path


#{ 
 # Driver Code Starts

if __name__ == '__main__':
    T=int(input())
    while T>0:
        V,E=map(int,input().split())
        adj=[[] for i in range(V+1)]
        for i in range(E):
            u,v=map(int,input().split())
            adj[u].append(v)
            adj[v].append(u)
        ob=Solution()
        ans=ob.dfsOfGraph(V,adj)
        for i in range(len(ans)):
            print(ans[i],end=" ")
        print()
        T-=1
# } Driver Code Ends