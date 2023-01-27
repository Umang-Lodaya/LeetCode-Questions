class Solution:
    def rob(self, nums: List[int]) -> int:
        n = len(nums)

        if n == 0: 
            return 0
        
        robNextPlusOne = 0
        robNext = nums[n - 1]

        for i in range(n - 2, -1, -1):
            current = max(robNext, robNextPlusOne + nums[i])
            robNextPlusOne = robNext
            robNext = current
        
        return robNext