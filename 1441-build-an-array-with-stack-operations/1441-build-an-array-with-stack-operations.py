class Solution:
    def buildArray(self, target: List[int], n: int) -> List[str]:
        sett = [False] * (n + 1)
        for i in target:
            sett[i] = True
        
        ans = []
        for i in range(1, target[-1] + 1):
            ans.append("Push")
            if not sett[i]:
                ans.append("Pop")
            
        return ans