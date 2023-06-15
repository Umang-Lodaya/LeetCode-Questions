class Solution:
    def largestAltitude(self, gain: List[int]) -> int:
        ls=[]
        k = 0
        ls.append(k)
        
        for x in range(len(gain)):
            k += gain[x]
            ls.append(k)
            
        return max(ls)