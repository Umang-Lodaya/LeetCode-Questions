class Solution:
    def containsDuplicate(self, nums: List[int]) -> bool:
        
        hashmap = {}
        for i in nums:
            if i not in hashmap:
                hashmap[i] = 1
            else:
                return True
        
        return False