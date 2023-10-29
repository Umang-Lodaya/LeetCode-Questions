class Solution:
    def floodFill(self, image: List[List[int]], sr: int, sc: int, color: int) -> List[List[int]]:
        m, n = len(image), len(image[0])
        
        changes = [[-1, 0], [1, 0], [0, -1], [0, 1]]
        
        if image[sr][sc] == color:
            return image
        
        startColor = image[sr][sc]
        image[sr][sc] = color
        
        queue = [[sr, sc]]
        while queue:
            for _ in range(len(queue)):
                i, j = queue.pop(0)
                for di, dj in changes:
                    ni, nj = i + di, j + dj
                    if 0 <= ni <= m - 1 and 0 <= nj <= n - 1:
                        if image[ni][nj] == startColor:
                            image[ni][nj] = color
                            queue.append([ni, nj])
                
                image[i][j] = color
        
        return image