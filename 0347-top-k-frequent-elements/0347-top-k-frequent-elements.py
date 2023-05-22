class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        freq = []
        for i in set(nums):
            freq.append([i, nums.count(i)])
        
        
        freq = sorted(freq, key=lambda x:x[1], reverse=True)
        
        freq = [freq[i][0] for i in range(k)]
        
        return freq