class Solution:
    def maxProduct(self, nums: List[int]) -> int:
        result = nums[0]
        currMax = nums[0]
        currMin = nums[0]

        for i in range(1, len(nums)):
            localMax = max(currMax * nums[i], nums[i], currMin * nums[i])
            localMin = min(currMax * nums[i], nums[i], currMin * nums[i])

            currMax = max(localMax, localMin)
            currMin = min(localMax, localMin)

            result = max(result, currMax)

        return result