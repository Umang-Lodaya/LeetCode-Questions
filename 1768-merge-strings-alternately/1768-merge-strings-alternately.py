class Solution:
    def mergeAlternately(self, word1: str, word2: str) -> str:
        m = min(len(word1), len(word2))
        
        result = ""
        for i in range(m):
            result += word1[i]
            result += word2[i]
        
        if word1[m:]:
            result += word1[m:]
        elif word2[m:]:
            result += word2[m:]
        
        return result