class Solution:
    def lemonadeChange(self, bills: List[int]) -> bool:
        BILLS = {5: 0, 10: 0}
        
        if len(BILLS) == 1 and BILLS[0] in [10, 20]:
            return False
        
        for i, bill in enumerate(bills):
            if bill == 5:
                BILLS[bill] += 1
                
            elif bill == 10:
                if BILLS[5] < 1:
                    return False
                BILLS[5] -= 1
                BILLS[10] += 1
            
            else:
                if BILLS[5] >= 1 and BILLS[10] >= 1:
                    BILLS[5] -= 1
                    BILLS[10] -= 1
                elif BILLS[5] >= 3:
                    BILLS[5] -= 3
                else:
                    return False
                
        return True