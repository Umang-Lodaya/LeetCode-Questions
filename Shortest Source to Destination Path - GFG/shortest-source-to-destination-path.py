#User function Template for python3
from collections import deque

class Solution:
    def shortestDistance(self, N, M, A, X, Y):
        if A[0][0] == 0 or A[X][Y] == 0:
            return -1
        
        visited = [[False for i in range(M)] for i in range(N)]
        delrow = [-1, 0, 1, 0]
        delcol = [0, 1, 0, -1]
        
        def isvalid(r, c):
            return (r >= 0 and r < N and c >= 0 and c < M)
        
        q = []
        q.append((0, 0, 0))
        
        while q:
            dist, row, col = q.pop(0)
            visited[row][col] = True
            if row == X and col == Y:
                return dist
            for i in range(4):
                r = row + delrow[i]
                c = col + delcol[i]
                if isvalid(r,c) and visited[r][c] == False and A[r][c] == 1:
                    visited[r][c] = 1
                    q.append((dist + 1, r, c))
        
        return -1


#{ 
 # Driver Code Starts

#Initial Template for Python 3

import math
        
if __name__=='__main__':
    t=int(input())
    for _ in range(t):
        N,M=map(int,input().strip().split())
        a=[]
        for i in range(N):
            s=list(map(int,input().strip().split()))
            a.append(s)
        x,y=map(int,input().strip().split())    
        ob=Solution()
        print(ob.shortestDistance(N,M,a,x,y))
        
# } Driver Code Ends