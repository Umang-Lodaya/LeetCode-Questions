class Solution:
    def rotate(self, nums: List[int], k: int) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """
        k = k % len(nums)
        
        while k > 0:
            last = nums.pop(-1)
            nums.insert(0, last)
            k -= 1