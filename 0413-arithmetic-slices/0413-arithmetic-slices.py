class Solution:
    def numberOfArithmeticSlices(self, nums: List[int]) -> int:
        if len(nums)<3: return 0
        start, l, r = 0, 0, 1
        diff = nums[r] - nums[l]
        ans = []
        while r < len(nums):
            if nums[r] - nums[l] == diff:
                l += 1
                r += 1
            else:
                ans.append(r - start)
                start = l
                diff = nums[r] - nums[l]
        
        ans.append(r - start)
        tot = 0
        for i in ans:
            if i>2:
                cur=i-2
                tot+=((cur+1)/2)*cur
        return int(tot)