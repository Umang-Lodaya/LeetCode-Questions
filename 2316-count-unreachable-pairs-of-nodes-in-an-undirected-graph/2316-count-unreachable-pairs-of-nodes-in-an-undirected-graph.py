class Solution(object):
    def countPairs(self, n, edges):
        neighbors = [[] for _ in range(n)]
        for edge in edges:
            neighbors[edge[0]].append(edge[1])
            neighbors[edge[1]].append(edge[0])

        visited = [False] * n
        sum_, squaresum = 0, 0

        for i in range(n):
            if not visited[i]:
                ans = self.dfs(i, neighbors, visited)
                sum_ += ans
                squaresum += ans * ans

        return (sum_ * sum_ - squaresum) // 2

    def dfs(self, node, neighbors, visited):
        visited[node] = True
        ans = 1

        for neighbor in neighbors[node]:
            if not visited[neighbor]:
                ans += self.dfs(neighbor, neighbors, visited)

        return ans