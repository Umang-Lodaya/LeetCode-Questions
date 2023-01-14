class Solution(object):
    def getRow(self, rowIndex):
        """
        :type rowIndex: int
        :rtype: List[int]
        """
        def fact(n):
            p = 1
            for i in range(2, n+1):
                p *= i
            return p
        
        def nCr(n, r):
            return fact(n) // (fact(r) * fact(n-r))
        
        if rowIndex == 0:
            return [1]
        
        ls = []
        for i in range(rowIndex+1):
            ls.append(nCr(rowIndex, i))
            
        return ls