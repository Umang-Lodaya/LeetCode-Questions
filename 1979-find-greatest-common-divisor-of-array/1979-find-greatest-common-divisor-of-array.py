class Solution:
    def findGCD(self, nums: List[int]) -> int:
        A = max(nums)
        B = min(nums)
        
        while B:
            A, B = B, A%B
        
        return A