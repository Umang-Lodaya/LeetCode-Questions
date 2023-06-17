class Solution:
    def findTheDifference(self, s: str, t: str) -> str:
        freq = {}
        for i in s:
            if i not in freq:
                freq[i] = 0
            freq[i] += 1
        
        for i in t:
            if i not in freq:
                return i
            freq[i] -= 1
        
        for i in freq:
            if freq[i] == -1:
                return i