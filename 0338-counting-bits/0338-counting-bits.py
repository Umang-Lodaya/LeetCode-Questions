class Solution:
    def countBits(self, n: int) -> List[int]:
        result = []
        
        for i in range(0, n + 1):
            b = bin(i)[2:]
            result.append(list(b).count('1'))
        
        return result