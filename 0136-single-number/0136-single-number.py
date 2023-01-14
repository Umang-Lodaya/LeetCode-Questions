class Solution:
    def singleNumber(self, nums: List[int]) -> int:
        odd = 0
        for i in nums:
            odd ^= i
        
        return odd