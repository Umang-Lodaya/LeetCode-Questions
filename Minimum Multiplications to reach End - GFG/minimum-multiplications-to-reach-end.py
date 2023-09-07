#User function Template for python3
from typing import List
 
class Solution:
    def minimumMultiplications(self, arr : List[int], start : int, end : int) -> int:
        if start == end:
            return 0
            
        max_level = 1500
        cur_level = 0
        visited = {start}
        queue = [[start, cur_level]]
        while cur_level < max_level:
            if len(queue) == 0:
                return -1
                
            cur_num, cur_level = queue.pop(0)
            new_level = cur_level + 1
            
            for num in arr:
                new_num = (cur_num * num)%100000
                if new_num == end:
                    return new_level
                
                if new_num not in visited:
                    queue.append([new_num, new_level])
                    visited.add(new_num)
        
        return -1

#{ 
 # Driver Code Starts
#Initial Template for Python 3

if __name__=="__main__":
    for _ in range(int(input())):
        n = int(input())
        arr = [int(x) for x in input().strip().split()]
        start, end = list(map(int,input().split()))
        obj=Solution()
        print(obj.minimumMultiplications(arr, start, end))
# } Driver Code Ends