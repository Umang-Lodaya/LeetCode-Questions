class Solution:
    def reverseVowels(self, s: str) -> str:
        loc = []
        s = list(s)
        
        for i in range(len(s)):
            if(s[i] in "aeiouAEIOU"):
                loc.append(i)
                
        for i in range(len(loc)//2):
            s[loc[i]], s[loc[-i - 1]] = s[loc[-i - 1]], s[loc[i]]
            
        return "".join(s)