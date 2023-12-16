class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        if len(s) != len(t):
            return False
        
        if s == t == "":
            return True
        
        if s == "" or t == "":
            return False
        
        freq = {}
        for char in s:
            freq[char] = freq.get(char, 0) + 1
        
        for char in t:
            if not freq.get(char, False) or freq[char] == 0:
                return False
            freq[char] -= 1
        
        return True