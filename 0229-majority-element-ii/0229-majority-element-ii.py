class Solution:
    def majorityElement(self, nums: List[int]) -> List[int]:
        if len(nums) == 1:
            return nums
        
        freq = {}
        ans = []
        for i in nums:
            if i not in freq:
                freq[i] = 1
            
            else:
                freq[i] += 1
                
        for i in freq.keys():
            if freq[i] > len(nums)//3:
                ans.append(i)
        
        return ans