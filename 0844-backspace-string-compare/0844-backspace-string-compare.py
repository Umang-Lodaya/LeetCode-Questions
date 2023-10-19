class Solution:
    def backspaceCompare(self, s: str, t: str) -> bool:
        def convertString(string):
            stack = []
            for char in string:
                if char == '#':
                    if not stack:
                        continue
                    stack.pop(-1)
                else:
                    stack.append(char)
            
            return "".join(stack)
        
        return convertString(s) == convertString(t)