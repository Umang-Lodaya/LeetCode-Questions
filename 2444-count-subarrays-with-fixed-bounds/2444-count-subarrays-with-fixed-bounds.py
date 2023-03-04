class Solution:
    def countSubarrays(self, nums: List[int], minK: int, maxK: int) -> int:
        ans = 0 # initialize answer variable to 0
        j = -1 # initialize starting index of current subarray to -1
        prevMinKIndex = -1 # initialize most recent index of minK to -1
        prevMaxKIndex = -1 # initialize most recent index of maxK to -1

        for i, num in enumerate(nums): # iterate over every element in nums with their index
            if num < minK or num > maxK:
                j = i # if nums[i] is out of range, move starting index of current subarray to i
            if num == minK:
                prevMinKIndex = i # if nums[i] is minK, update most recent index of minK to i
            if num == maxK:
                prevMaxKIndex = i # if nums[i] is maxK, update most recent index of maxK to i

          # calculate number of valid subarrays that end at index i and add to answer
            ans += max(0, min(prevMinKIndex, prevMaxKIndex) - j)

        return ans # return the total count of valid subarrays