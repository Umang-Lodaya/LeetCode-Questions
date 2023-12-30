class Solution:
    def makeEqual(self, words: List[str]) -> bool:
        n = len(words)
        if n == 1: return True
        
        freq = {}
        for word in words:
            for char in word:
                freq[char] = freq.get(char, 0) + 1
        
        for k, v in freq.items():
            if v % n != 0:
                return False
        
        return True