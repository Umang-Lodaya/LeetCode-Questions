class Solution:
    def largestAltitude(self, gain: List[int]) -> int:
        ans = 0
        k = 0
        
        for x in range(len(gain)):
            k += gain[x]
            ans = max(ans, k)
            
        return ans