class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        
        def myStr(string):
            l = list(string)
            l.sort()
            return ''.join(l)
        
        hashh = {}
        for i in strs:
            if myStr(i) in hashh:
                hashh[myStr(i)].append(i)
            else:
                hashh[myStr(i)] = [i]
                
        return list(hashh.values())