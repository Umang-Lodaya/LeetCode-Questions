class Solution:
    def bulbSwitch(self, n: int) -> int:
        left = 1
        right = n
        result = 0

        while left <= right:
            mid = left + (right - left) // 2
            square = mid * mid

            if square == n:
                return mid
            elif square < n:
                left = mid + 1
                result = mid
            else:
                right = mid - 1

        return result