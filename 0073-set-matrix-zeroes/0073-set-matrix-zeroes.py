class Solution:
    def setZeroes(self, matrix: List[List[int]]) -> None:
        """
        Do not return anything, modify matrix in-place instead.
        """
        n_rows = len(matrix)
        n_cols = len(matrix[0])
        
        isFirstRowZero = False
        isFirstColZero = False
        
        for row in range(n_rows):
            if matrix[row][0] == 0:
                isFirstColZero = True
                break
        
        for col in range(n_cols):
            if matrix[0][col] == 0:
                isFirstRowZero = True
                break
        
        for row in range(1, n_rows):
            for col in range(1, n_cols):
                if matrix[row][col] == 0:
                    matrix[row][0] = 0
                    matrix[0][col] = 0
        
        for row in range(1, n_rows):
            for col in range(1, n_cols):
                if matrix[row][0] == 0 or matrix[0][col] == 0:
                    matrix[row][col] = 0
        
        if isFirstRowZero:
            for col in range(n_cols):
                matrix[0][col] = 0
                
        if isFirstColZero:
            for row in range(n_rows):
                matrix[row][0] = 0
                
        for row in matrix:
            print(row)