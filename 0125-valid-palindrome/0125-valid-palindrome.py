import re

class Solution:
    def isPalindrome(self, s: str) -> bool:
        s = s.lower()
        s = re.sub('[^0-9a-zA-Z]+', '', s)
        
        if s == "":
            return True
        
        i = 0
        while i < len(s) // 2:
            if s[i] != s[len(s) - 1 - i]:
                return False
            i += 1
            
        return True