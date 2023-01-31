class Solution:
    def findBall(self, grid: List[List[int]]) -> List[int]:
        N = len(grid[0])-1
        output = list(range(N+1))
        
        for i in range(len(grid)):
            for index,pos in enumerate(output):
                if pos == -1 :
                    continue
                if ((pos == 0 and grid[i][pos]==-1) or
                    (pos == N and grid[i][pos] == 1)):
                    output[index] = -1
                    
                elif grid[i][pos] == 1 and grid[i][pos] + grid[i][pos+1] != 0:
                    output[index] += 1
                    
                elif grid[i][pos] == -1 and grid[i][pos] + grid[i][pos-1] != 0:
                    output[index] -= 1
                    
                else:
                    output[index] = -1
        return output