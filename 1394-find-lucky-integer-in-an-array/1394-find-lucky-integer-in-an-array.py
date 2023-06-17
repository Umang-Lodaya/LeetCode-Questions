class Solution:
    def findLucky(self, arr: List[int]) -> int:
        freq = {}
        for i in arr:
            if i not in freq:
                freq[i] = 0
            freq[i] += 1
        
        ans = -1
        for i in freq:
            if i == freq[i]:
                ans = max(ans, i)
        
        return ans