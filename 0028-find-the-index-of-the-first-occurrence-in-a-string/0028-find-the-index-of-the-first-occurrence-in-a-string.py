class Solution:
    def strStr(self, haystack: str, needle: str) -> int:
        n = len(haystack)
        m = len(needle)
        
        if m == 0:
            return 0
        
        pi = [0] * m
        j = 0
        
        for i in range(1, m):
            while j > 0 and needle[j] != needle[i]:
                j = pi[j - 1]
            if needle[j] == needle[i]:
                j += 1
            pi[i] = j
        
        j = 0
        
        for i in range(n):
            while j > 0 and needle[j] != haystack[i]:
                j = pi[j - 1]
            if needle[j] == haystack[i]:
                j += 1
            if j == m:
                return i - m + 1
        
        return -1