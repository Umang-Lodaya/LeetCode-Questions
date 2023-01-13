class Solution:
    def longestCommonPrefix(self, strs: List[str]) -> str:
        
        common = min(strs, key=len)
        for item in strs:
            while len(common) > 0:
                if item.startswith(common):
                    break
                else:
                    common = common[:-1] 
                    
        return common