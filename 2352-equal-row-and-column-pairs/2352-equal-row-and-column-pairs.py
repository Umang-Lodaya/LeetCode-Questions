class Solution:
    def equalPairs(self, grid: List[List[int]]) -> int:
        count = 0
        for row in range(len(grid)):
            for col in range(len(grid[0])):
                if grid[row] == [grid[i][col] for i in range(len(grid))]:
                    count += 1
        
        return count