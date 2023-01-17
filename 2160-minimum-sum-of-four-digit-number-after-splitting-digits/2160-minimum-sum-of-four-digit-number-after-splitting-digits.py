class Solution:
    def minimumSum(self, num: int) -> int:
        num = str(num)
        num_lst = [int(x) for x in num]
        num_lst.sort()
        
        num1 = list()
        num2 = list()
        num1_boolean = True
        
        for i in num_lst:
            if num1_boolean == True:
                num1.append(i)
                num1_boolean = False
            else:
                num2.append(i)
                num1_boolean = True
                
        num1 = [str(x) for x in num1]
        num2 = [str(x) for x in num2]
        
        num1 = int(''.join(num1))
        num2 = int(''.join(num2))
        
        return num1 + num2