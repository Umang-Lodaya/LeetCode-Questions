class Solution(object):
    def mySqrt(self, x):
        """
        :type x: int
        :rtype: int
        """
        low = 0
        high = x//2 + 1
        while low < high:
            mid = (high + low + 1) // 2
            if mid * mid > x:
                high = mid - 1
            else:
                low = mid

        return low