class Solution:
    def numberOfWays(self, corridor: str) -> int:
        seatsToLeft = 0        
        consecutivePlants = 0
        ans = 1
            
        for c in corridor:
            if c == "P":
                if seatsToLeft and seatsToLeft % 2 == 0:
                    consecutivePlants += 1
            else:
                seatsToLeft += 1
            
                if seatsToLeft % 2 == 1 and consecutivePlants != 0:
                    ans *= (consecutivePlants+1)
                    consecutivePlants = 0
                
        return ans%(10**9+7) if (seatsToLeft and seatsToLeft%2 == 0) else 0