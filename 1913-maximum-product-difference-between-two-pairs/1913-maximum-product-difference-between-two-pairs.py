class Solution:
    def maxProductDifference(self, nums: List[int]) -> int:
        nums.sort()
        a, b = nums[-2:]
        c, d = nums[:2]
        
        return a*b - c*d