class Solution:
    def longestSubarray(self, nums: List[int]) -> int:
        prev = 0
        curr = 0
        ans = 0
        for i in nums:
            if i == 1:
                curr += 1
            else:
                ans = max(ans, curr + prev)
                prev = curr
                curr = 0
        ans = max(ans, curr + prev)

        return ans-1 if ans == len(nums) else ans