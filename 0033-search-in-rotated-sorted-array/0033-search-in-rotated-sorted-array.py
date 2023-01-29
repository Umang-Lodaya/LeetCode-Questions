class Solution:
    def search(self, nums: List[int], target: int) -> int:
        return searchlist(nums,target)
      
def searchlist(nums,target):
    low, high = 0, len(nums) - 1
    while low <= high:
        mid = low + (high - low) // 2
        if nums[mid] == target:
            return mid

        if nums[mid] >= nums[low]:
            if target >= nums[low] and target < nums[mid]:
                high = mid - 1
            else:
                low = mid + 1

        else:
            if target <= nums[high] and target > nums[mid]:
                low = mid + 1
            else:
                high = mid - 1

    return -1 