class Solution:
    def arraySign(self, nums: List[int]) -> int:
        i = 0
        for num in nums:
            if num == 0:
                return 0
            if num < 0:
                i += 1
        
        return 1 if i%2==0 else -1