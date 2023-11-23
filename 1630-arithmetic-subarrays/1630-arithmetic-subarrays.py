class Solution:
    def checkArithmeticSubarrays(self, nums: List[int], l: List[int], r: List[int]) -> List[bool]:
        ans = []
        for i, j in zip(l, r):
            arr = nums[i:j + 1]
            ans.append(self.Arithmetic(arr))
        
        return ans
    
    def Arithmetic(self, arr):
        if len(arr) <= 2:
            return True
        arr.sort()
        d = arr[1] - arr[0]
        for inx in range(2, len(arr)):
            cd = arr[inx] - arr[inx - 1]
            if cd != d:
                return False
        
        return True