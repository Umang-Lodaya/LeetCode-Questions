class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        nums.sort()
        
        ans = set()
        for i in range(len(nums)):
            j = i + 1; k = len(nums) - 1
            while j < k:
                s = nums[i] + nums[j] + nums[k]
                if s == 0:
                    ans.add((nums[i], nums[j], nums[k]))
                    j += 1
                    k -= 1
                elif s < 0:
                    j += 1
                else:
                    k -= 1
        
        return list(ans)