class Solution:
    def addDigits(self, num: int) -> int:
        if len(str(num)) == 1:
            return num
        
        while (len(str(num)) != 1):
            num = sum([int(x) for x in str(num)])
        
        return num