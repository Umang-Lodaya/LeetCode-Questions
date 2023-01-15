class Solution:
    def majorityElement(self, nums: List[int]) -> int:
        
        if len(nums) == 1:
            return nums[0]
        
        freq = {}
        for i in nums:
            if i not in freq:
                freq[i] = 1
            
            else:
                freq[i] += 1
                if freq[i] > len(nums)//2:
                    return i