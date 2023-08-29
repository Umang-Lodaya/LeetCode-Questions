class Solution:
    def bestClosingTime(self, customers: str) -> int:
        best = -1; maxx = 0
        curr = 0
        
        for i, e in enumerate(customers):
            if e == 'Y':
                curr += 1
            else:
                curr -= 1
            
            if curr > maxx:
                maxx = curr
                best = i
        
        return best + 1