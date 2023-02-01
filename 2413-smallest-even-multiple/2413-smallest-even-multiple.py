class Solution:
    def smallestEvenMultiple(self, n: int) -> int:
        if n in [1, 2]:
            return 2
        
        def gcd(X, Y):
            if Y == 0:
                return X
            return gcd(Y, X%Y)
        
        return n*2//gcd(n, 2)