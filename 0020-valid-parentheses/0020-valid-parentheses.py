class Solution:
    def isValid(self, s: str) -> bool:
        if len(s)%2 != 0:
            return False
        
        parn = {'(':')', '[':']', '{':'}'}
        stack = []
        for char in s:
            if char in parn.keys():
                stack.append(char)
            elif stack == []:
                return False
            else:
                open = stack.pop()
                if(parn[open] != char):
                    return False
                
        if(len(stack)>0):
            return False
        
        return True