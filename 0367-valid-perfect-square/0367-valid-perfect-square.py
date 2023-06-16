class Solution:
    def isPerfectSquare(self, num: int) -> bool:
        left = 1
        right = num
        
        while left <= right:
            mid = left + (right - left) // 2
            sq = mid * mid
            
            if sq == num:
                return True
            elif sq > num:
                right = mid - 1
            else:
                left = mid + 1
        
        return False