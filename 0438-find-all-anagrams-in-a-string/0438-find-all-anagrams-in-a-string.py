from collections import Counter

class Solution:
    def findAnagrams(self, s: str, p: str) -> List[int]:
        n1, n2 = len(s), len(p)
        d1 = Counter(p)
        d2 = Counter(s[:n2-1])
        ans = []
        j = 0
        
        for i in range(n2-1,n1):
            d2[s[i]] += 1
            if d1 == d2:
                ans.append(j)
            
            d2[s[j]] -= 1
            if d2[s[j]] == 0:
                del d2[s[j]]
            j += 1

        return ans