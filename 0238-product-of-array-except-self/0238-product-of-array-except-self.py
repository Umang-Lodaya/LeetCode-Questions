class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        n = len(nums)
        if n == 2:
            return nums[::-1]
        
        prefix = [1 for _ in range(n)]
        suffix = [1 for _ in range(n)]
        p = 1; s = 1
        
        for i in range(n):
            prefix[i] = p
            suffix[n - 1 - i] = s
            p *= nums[i]
            s *= nums[n - 1 - i]
        
        arr = [prefix[i] * suffix[i] for i in range(n)]
        print(arr)
        return arr