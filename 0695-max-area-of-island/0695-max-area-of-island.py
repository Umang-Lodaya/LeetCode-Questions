class Solution:
    def maxAreaOfIsland(self, grid: List[List[int]]) -> int:
        M, N = len(grid), len(grid[0])                                          
        
        
        def isValidIndice(row: int, column: int) -> bool:                       
            if row < 0 or M <= row: return False                                
            if column < 0 or N <= column: return False                          
            
            return True                                                         
        
        def islandArea(row, column) -> int:                                     
            if not isValidIndice(row, column): return 0                         
            if grid[row][column] == 0: return 0                                 
            
            grid[row][column] = 0                                               
            up, down = islandArea(row-1, column), islandArea(row+1, column)     
            left, right = islandArea(row, column-1), islandArea(row, column+1)  
            
            return 1 + up + down + left + right                                 
            
        area, maxArea = 0, 0
        for row in range(M):                                                    
            for column in range(N):                                             
                area = islandArea(row, column)                                  
                maxArea = max(maxArea, area)                                    
                
        return maxArea                                                          