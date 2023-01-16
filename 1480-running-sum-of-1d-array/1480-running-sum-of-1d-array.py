class Solution:
    def runningSum(self, nums: List[int]) -> List[int]:
        
        result = [0]*len(nums)
        
        for i in range(len(nums)):
            result[i] = sum(nums[:i+1])
        
        return result