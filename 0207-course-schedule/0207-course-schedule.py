class Solution:
    def canFinish(self, numCourses: int, prerequisites: List[List[int]]) -> bool:
        preReq = {i: [] for i in range(numCourses)}
        for curr, pre in prerequisites:
            preReq[curr].append(pre)
        
        cycle = [False for i in range(numCourses)]
        visited = [False for i in range(numCourses)]
        output = []
        
        def dfs(node):
            if cycle[node]:
                return False
            
            if visited[node]:
                return True
            
            cycle[node] = True
            visited[node] = True
            for pre in preReq[node]:
                if dfs(pre) == False:
                    return False
            
            cycle[node] = False
            output.append(node)
            return True
        
        for i in range(numCourses):
            if dfs(i) == False:
                return False
        
        print(output)
        return True