class Solution:
    def shuffle(self, nums, n):
        first = 0
        second = n
        max_val = 10000
        
        for i in range(2 * n):
            if i % 2 == 0:
                nums[i] = (nums[first] % max_val) * max_val + nums[i]
                first += 1
            else:
                nums[i] = (nums[second] % max_val) * max_val + nums[i]
                second += 1
        
        for i in range(2 * n):
            nums[i] = nums[i] // max_val
        
        return nums