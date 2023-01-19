class Solution:
    def subarraysDivByK(self, nums: List[int], k: int) -> int:
        counts = [0]*k
        s = 0
        
        for i in nums:
            s += i%k
            counts[s % k] += 1
        
        res = counts[0]
        for c in counts:
            res += c * (c-1) // 2
        
        return res