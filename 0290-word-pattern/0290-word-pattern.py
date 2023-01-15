class Solution:
    def wordPattern(self, pattern: str, s: str) -> bool:
        
        if len(pattern) != len(s.split()) or len(set(list(pattern))) != len(set(s.split())):
            return False
        
        mappings = {}
        for p,s in zip(pattern, s.split()):
            
            if p not in mappings:
                mappings[p] = [s]
            else:
                mappings[p].append(s)
        
        for key in mappings:
            if len(set(mappings[key])) != 1:
                return False
            
        return True