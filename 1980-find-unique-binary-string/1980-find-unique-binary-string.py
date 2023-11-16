class Solution:
    def findDifferentBinaryString(self, nums):
        ans = ""

        for i in range(len(nums)):
            currentChar = nums[i][i]
            oppositeChar = '1' if currentChar == '0' else '0'

            ans += oppositeChar

        return ans