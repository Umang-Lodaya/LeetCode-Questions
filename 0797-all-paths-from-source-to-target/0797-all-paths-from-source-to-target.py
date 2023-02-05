class Solution:
    def allPathsSourceTarget(self, graph: List[List[int]]) -> List[List[int]]:
        target = len(graph) - 1
        paths, targets = [[0]], []
        
        while paths:
            path = paths.pop(0)
            edges = graph[path[-1]]
            if not edges: 
                continue
            for edge in edges:
                if edge==target:
                    targets.append(path+[edge])
                else:
                    paths = [path+[edge]] + paths
        
        return targets 