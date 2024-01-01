class Solution:
    def maxLengthBetweenEqualCharacters(self, s: str) -> int:
        freq = {}
        isRepeated = set()
        for i, char in enumerate(s):
            if not freq.get(char, False):
                freq[char] = [i, i]
            else:
                freq[char][1] = i
                isRepeated.add(char)
        
        if not isRepeated:
            return -1
        
        ans = -1
        for char in list(isRepeated):
            ans = max(ans, freq[char][1] - freq[char][0] - 1)
        
        return ans