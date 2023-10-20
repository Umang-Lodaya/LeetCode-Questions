class Solution:
    def containsDuplicate(self, nums: List[int]) -> bool:
        freq = {}
        for i in nums:
            if freq.get(i, 0) >= 1:
                return True
            freq[i] = 1
        
        return False