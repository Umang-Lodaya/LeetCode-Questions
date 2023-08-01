#User function Template for python3

class Solution:
    
    #Function to return a list containing the DFS traversal of the graph.
    def dfsOfGraph(self, V, adj):
        def dfs(node, graph, visited, component):
            component.append(node)  # Store answer
            visited[node] = True  # Mark visited
        
            # Traverse to each adjacent node of a node
            for child in graph[node]:
                if not visited[child]:  # Check whether the node is visited or not
                    dfs(child, graph, visited, component)  # Call the dfs recursively
    
        node = 0  # Starting node
        visited = [False]*V  # Make all nodes to False initially
        component = []
        dfs(node, adj, visited, component)  # Traverse to each node of a graph
        return component

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