from typing import List


class Solution:
    def isFrequencyUnique(self, n : int, arr : List[int]) -> bool:
        freq = dict()
        uniq = set()
        for i in arr:
            freq[i] = freq.get(i, 0) + 1
        
        for val in freq.values():
            if val in uniq:
                return False
            uniq.add(val)
        
        return True
        

#{ 
 # Driver Code Starts

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
        
        n = int(input())
        
        
        arr=IntArray().Input(n)
        
        obj = Solution()
        res = obj.isFrequencyUnique(n, arr)
        
        result_val = 1 if res else 0
        print(result_val)

# } Driver Code Ends