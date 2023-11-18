class Solution:
    def maxFrequency(self, nums, k):
        nums.sort()
        length = len(nums)
        
        differences = [0] * length
        for i in range(1, length):
            differences[i] = nums[i] - nums[i - 1]

        prefix_sums = [0] * length
        for i in range(1, length):
            prefix_sums[i] = prefix_sums[i - 1] + differences[i]

        low, high = 1, length
        while low < high:
            mid = (high - low + 1) // 2 + low
            if self.isPossible(nums, differences, prefix_sums, mid, k):
                low = mid
            else:
                high = mid - 1

        return low
    
    def isPossible(self, nums, differences, prefix_sums, freq, k):
        length = len(differences)
        times = 0
        for i in range(freq - 2, -1, -1):
            times += nums[freq - 1] - nums[i]

        min_times = times
        for i in range(freq, length):
            times = times - (prefix_sums[i - 1] - prefix_sums[i - freq]) + differences[i] * (freq - 1)
            min_times = min(min_times, times)

        return min_times <= k