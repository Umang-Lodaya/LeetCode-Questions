class Solution:
    def orangesRotting(self, grid: List[List[int]]) -> int:
        m, n = len(grid), len(grid[0])
        changesDirections = [[-1, 0], [1, 0], [0, -1], [0, 1]]
        time = -1
        
        queue = []
        for i in range(m):
            for j in range(n):
                if grid[i][j] == 2:
                    queue.append([i, j])
        
        while queue:
            for _ in range(len(queue)):            
                i, j = queue.pop(0)
                for di, dj in changesDirections:
                    ni = i + di; nj = j + dj
                    if 0 <= ni <= m - 1 and 0 <= nj <= n - 1:
                        if grid[ni][nj] == 1:
                            grid[ni][nj] = 2
                            queue.append([ni, nj])
                
                grid[i][j] = 2
                
            time += 1
        
        for i in range(m):
            for j in range(n):
                if grid[i][j] == 1:
                    return -1
        
        return max(0, time)