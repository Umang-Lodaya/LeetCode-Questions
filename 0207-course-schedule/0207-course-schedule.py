class Solution:
    def canFinish(self, n: int, pre: List[List[int]]) -> bool:
        preReq = {i: [] for i in range(n)}
        for curr, p in pre:
            preReq[curr].append(p)
        
        cycle = [False for i in range(n)]
        visited = [False for i in range(n)]
        seq = []
        
        def dfs(node):
            if cycle[node]: return False
            if visited[node]: return True
            
            cycle[node] = True
            visited[node] = True
            
            for p in preReq[node]:
                if dfs(p) == False:
                    return False
            
            cycle[node] = False
            seq.append(node)
        
        for i in range(n):
            if dfs(i) == False:
                return False
        
        return True            