class Solution:
    def setZeroes(self, matrix: List[List[int]]) -> None:
        """
        Do not return anything, modify matrix in-place instead.
        """
        m, n = len(matrix), len(matrix[0])
        top = [False for j in range(n)]
        left = [False for i in range(m)]
        
        for i in range(m):
            for j in range(n):
                if matrix[i][j] == 0:
                    top[j] = True
                    left[i] = True
        
        for i in range(m):
            for j in range(n):
                if left[i] or top[j]:
                    matrix[i][j] = 0
        
        