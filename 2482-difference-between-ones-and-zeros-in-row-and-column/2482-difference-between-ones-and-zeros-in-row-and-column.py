class Solution:
    def onesMinusZeros(self, grid: List[List[int]]) -> List[List[int]]:
        m, n = len(grid), len(grid[0])
        onesRow = []; onesCol = []
        zeroRow = []; zeroCol = []
        
        for row in grid:
            s = sum(row)
            onesRow.append(s)
            zeroRow.append(n - s)
        
        for col in zip(*grid):
            s = sum(col)
            onesCol.append(s)
            zeroCol.append(m - s)
        
        print(onesRow, zeroRow)
        print(onesCol, zeroCol)
        
        diff = []
        for i in range(m):
            row = []
            for j in range(n):
                d = onesRow[i] + onesCol[j] - zeroRow[i] - zeroCol[j]
                row.append(d)
            diff.append(row)
        
        return diff