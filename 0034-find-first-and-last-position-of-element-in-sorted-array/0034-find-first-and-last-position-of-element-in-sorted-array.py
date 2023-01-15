class Solution:
    def getLeft(self, nums, target):
        l = 0
        r = len(nums) - 1
        
        while l <= r:
            mid = (l + r) // 2
            if nums[mid] == target:
                if mid-1 >= 0 and nums[mid - 1] != target or mid==0:
                    return mid
                r = mid - 1
            elif nums[mid] > target:
                r = mid - 1
            else:
                l = mid + 1
        
        return -1
    
    def getRight(self, nums, target):
        l = 0
        r = len(nums) - 1
        
        while l <= r:
            mid = (l + r) // 2
            if nums[mid] == target:
                if mid+1 < len(nums) and nums[mid+1] != target or mid==len(nums)-1:
                    return mid
                l = mid + 1
            elif nums[mid] > target:
                r = mid - 1
            else:
                l = mid + 1
        
        return -1
    
    def searchRange(self, nums: List[int], target: int) -> List[int]:
        
        return [self.getLeft(nums, target), self.getRight(nums, target)]