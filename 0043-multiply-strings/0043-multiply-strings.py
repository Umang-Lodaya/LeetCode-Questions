class Solution:
    def multiply(self, num1: str, num2: str) -> str:
        # return str(int(num1) * int(num2))
        n1 = 0
        j = 0
        for i in num1[::-1]:  
            n1 = int(i) * (10 ** j) + n1
            j += 1
        
        n2 = 0
        j = 0
        for i in num2[::-1]:  
            n2 = int(i) * (10 ** j) + n2
            j += 1
        
        return str(n1*n2)