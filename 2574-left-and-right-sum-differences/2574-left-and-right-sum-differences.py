class Solution:
    def leftRightDifference(self, nums: List[int]) -> List[int]:
        leftSum = [0]
        for i in range(1, len(nums)):
            leftSum.append(sum(nums[:i]))
        
        rightSum = []
        for i in range(len(nums)-1):
            rightSum.append(sum(nums[i+1:]))
        rightSum.append(0)
        
        ans = []
        for i, j in zip(leftSum, rightSum):
            ans.append(abs(i - j))
        
        return ans
        