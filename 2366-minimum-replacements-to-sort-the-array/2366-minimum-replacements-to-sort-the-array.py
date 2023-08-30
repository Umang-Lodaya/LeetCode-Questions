class Solution:
    def minimumReplacement(self, nums: List[int]) -> int:
        op = 0
        n = len(nums)
        last = nums[n-1]
        for i in range(n - 2, -1, -1):
            q, r = divmod(nums[i], last)
            if q == 0:
                last = r
            elif r == 0:
                op += q - 1
            else:
                op += q
                last -= (last - r + q) // (q + 1)
                #-=ceil((last-r)/(q+1))
        return op