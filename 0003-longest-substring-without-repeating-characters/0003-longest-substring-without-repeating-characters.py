class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        l, r = 0, 0
        
        hashmap = {}
        ans = 0
        while l < len(s) and r < len(s):
            e = s[r]
            if e in hashmap:
                l = max(l, hashmap[e]+1)
            
            hashmap[e] = r
            ans = max(ans, r-l+1)
            r += 1
        
        return ans