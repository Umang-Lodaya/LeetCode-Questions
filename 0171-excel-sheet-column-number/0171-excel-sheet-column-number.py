class Solution:
    def titleToNumber(self, columnTitle: str) -> int:
        ans, pos = 0, 0
        
        for letter in columnTitle[::-1]:
            digit = ord(letter) - ord('A') + 1
            ans += digit * 26**pos
            pos += 1
        
        return ans