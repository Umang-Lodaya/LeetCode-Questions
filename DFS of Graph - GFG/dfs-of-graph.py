#User function Template for python3

class Solution:
    
    def dfsOfGraph(self, V, adj):
        def dfs(node, graph, visited, component):
            component.append(node)
            visited[node] = True
        
            for child in graph[node]:
                if not visited[child]:  
                    dfs(child, graph, visited, component)
    
        node = 0  
        visited = [False]*V  
        component = []
        dfs(node, adj, visited, component)  
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