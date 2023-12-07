class Solution:
    def largestOddNumber(self, num: str) -> str:
        leng = len(num)
        for i, n in enumerate(num[::-1]):
            if int(n) % 2 != 0:
                return num[:leng - i]
            
        return ""
            
        """
        43210
        42076
        01234
        """