class Solution:
    def countNegatives(self, grid: List[List[int]]) -> int:
        count = 0
        for row in grid:
            for col in row[::-1]:
                if col >= 0:
                    break
                count += 1
        
        return count