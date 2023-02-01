class Solution:
    def backspaceCompare(self, s, t):
        p1 = len(s)-1   
        p2 = len(t)-1   
        while p1 >=0 or p2 >= 0:
            if (p1 >= 0 and s[p1] == '#') or (p2 >= 0 and t[p2] =='#'):
                if s[p1] =='#':
                    backcount = 2
                    while backcount > 0:
                        p1 -=1   
                        backcount -= 1   
                        if p1 >=0 and s[p1] == '#':
                            backcount += 2
                if t[p2] =='#':
                    backcount = 2 
                    while backcount > 0:
                        p2 -=1
                        backcount -= 1
                        if p2 >= 0 and t[p2] =='#':
                            backcount +=2
            else:
                if p1 <0 or p2 <0:
                    return False
                elif s[p1] != t[p2]:
                    return False
                else:
                    p1 -= 1
                    p2 -= 1
        return True