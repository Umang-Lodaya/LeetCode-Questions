class Solution:
    def missingNumber(self, nums: List[int]) -> int:
        odd = len(nums)
        for i in range(len(nums)):
            odd ^= i
            odd ^= nums[i]
            
        return odd