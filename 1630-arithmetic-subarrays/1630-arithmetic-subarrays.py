class Solution:
    def checkArithmeticSubarrays(self, nums: List[int], l: List[int], r: List[int]) -> List[bool]:
        ans = []
        for i, j in zip(l, r):
            arr = nums[i:j + 1]
            ans.append(self.isArithmetic(arr))
        
        return ans
    
    def isArithmetic(self, arr):
        if len(arr) <= 2:
            return True
        arr.sort()
        cd = arr[1] - arr[0]
        for inx in range(2, len(arr)):
            d = arr[inx] - arr[inx - 1]
            if d != cd:
                return False
        
        return True