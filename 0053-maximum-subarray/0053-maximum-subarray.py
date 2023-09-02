class Solution:
    def maxSubArray(self, nums: List[int]) -> int:
        curr = 0
        max = -99999
        for i in range(len(nums)):
            curr += nums[i]
            if curr > max:
                max = curr
                
            if curr < 0:
                curr = 0
                
        return max