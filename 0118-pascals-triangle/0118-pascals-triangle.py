class Solution:
    def generate(self, numRows: int) -> List[List[int]]:
        C = []
        for num in range(1, numRows+1):
            ls = []
            for i in range(num):
                if(i == 0 or i==num-1):
                    ls.append(1)
                else:
                    e = C[num-2][i-1] + C[num-2][i]
                    ls.append(e)
            
        
            C.append(ls)
        return C