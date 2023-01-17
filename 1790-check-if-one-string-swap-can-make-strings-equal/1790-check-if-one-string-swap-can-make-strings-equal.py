class Solution:
    def areAlmostEqual(self, s1: str, s2: str) -> bool:
        if(s1 == s2):
            return True
        if(len(s1) != len(s2)):
            return False
        
        for i in range(len(s2)-1):
            for j in range(i+1, len(s2)):        
                s2_list = list(s2)
                s2_list[i], s2_list[j] = s2_list[j], s2_list[i]
                ms2 = ''.join(s2_list)
                
                if(ms2 == s1):
                    return True
                       
        return False