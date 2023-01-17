class Solution:
    def digitSum(self, s: str, k: int) -> str:
        while len(s) > k:
            ls = []
            while(str(s)!=''):
                ls.append(s[:k])
                s = s[k:]

            sumList = []
            for i in ls:
                sumList.append(str(sum([int(x) for x in i])))

            s = ''.join(sumList)
        
        return s