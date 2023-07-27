class Solution:
    def maxRunTime(self, n: int, batteries: List[int]) -> int:
        left = 0
        right = sum(batteries) // n+1
        
        check = lambda time: sum(min(time, b) for b in batteries) >= (n * time)

        while left <= right:
            mid = left + (right - left) // 2
            if check(mid):
                left = mid + 1
            else:
                right = mid - 1

        return right 