#User function Template for python3
import math
from typing import List

class Solution:
    def shortestPath(self, n : int, m : int, edges : List[List[int]]) -> List[int]:
        dist = {v: math.inf for v in range(n)}
        dist[0] = 0
        
        Q = list(range(n))
        
        while Q:
            u = min(Q, key=dist.get)
            Q.remove(u)
        
            neib = [(x,y,d) for (x,y,d) in edges if x==u and y in Q]
            
            for (u,v,d) in neib:
                alt = dist[u] + d
                if alt < dist[v]:
                    dist[v] = alt
                    
        return list(map(lambda x: -1 if x==math.inf else x, dist.values()))


#{ 
 # Driver Code Starts

#Initial Template for Python 3

from typing import List




class IntMatrix:
    def __init__(self) -> None:
        pass
    def Input(self,n,m):
        matrix=[]
        #matrix input
        for _ in range(n):
            matrix.append([int(i) for i in input().strip().split()])
        return matrix
    def Print(self,arr):
        for i in arr:
            for j in i:
                print(j,end=" ")
            print()



class IntArray:
    def __init__(self) -> None:
        pass
    def Input(self,n):
        arr=[int(i) for i in input().strip().split()]#array input
        return arr
    def Print(self,arr):
        for i in arr:
            print(i,end=" ")
        print()


if __name__=="__main__":
    t = int(input())
    for _ in range(t):
        
        n,m=map(int,input().split())
        
        
        edges=IntMatrix().Input(m, 3)
        
        obj = Solution()
        res = obj.shortestPath(n, m, edges)
        
        IntArray().Print(res)
# } Driver Code Ends