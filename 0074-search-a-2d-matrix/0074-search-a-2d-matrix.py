class Solution:
    def binarySearch(self, arr, target):
        l, r = 0, len(arr) - 1
        
        while(l <= r):
            mid = l + (r-l)//2
            
            if arr[mid] == target:
                return True
            
            if arr[mid] > target:
                r = mid - 1
            else:
                l = mid + 1
        
        return False
        
        
    def searchMatrix(self, matrix: List[List[int]], target: int) -> bool:
        for row in matrix:
            if target <= row[-1]:
                return self.binarySearch(row, target)