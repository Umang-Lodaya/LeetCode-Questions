class Solution:
    def fib(self, n: int) -> int:
        if n in [0,1]:
            return n
        
        a = 0; b = 1
        curr = 0
        for _ in range(n):
            curr = a + b
            b = a
            a = curr
        return curr