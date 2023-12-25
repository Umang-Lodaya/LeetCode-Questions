class Solution:
    def numDecodings(self, s: str) -> int:
        @lru_cache(None)
        def dfs(s):
            if not s: return 1
            if s[0] == '0': return 0
            if len(s) > 1 and int(s[:2]) < 27:
                return dfs(s[1:]) + dfs(s[2:])

            return dfs(s[1:])      
        
        return dfs(s)