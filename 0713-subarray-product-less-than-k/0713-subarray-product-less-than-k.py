class Solution:
    def numSubarrayProductLessThanK(self, nums: List[int], k: int) -> int:
        running_product = 1
        left = 0
        valid_subarrays_count = 0
        
        for right, value in enumerate(nums):
            running_product *= value
			
			# If we went over the product, decrease.
            while left < right and running_product >= k:
                running_product /= nums[left]
                left += 1
                
            if running_product < k:
                valid_subarrays_count += right - left + 1
            
        return valid_subarrays_count