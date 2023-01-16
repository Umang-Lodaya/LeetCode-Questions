class Solution:
    def fourSumCount(self, nums1: List[int], nums2: List[int], nums3: List[int], nums4: List[int]) -> int:
        freq = {}
        ans = 0
        for i in nums1:
            for j in nums2:
                
                if i+j not in freq:
                    freq[i+j] = 0
                
                freq[i+j] += 1
        
        for i in nums3:
            for j in nums4:
                if -(i+j) in freq:
                    ans += freq[-(i+j)]
        
        return ans
                    