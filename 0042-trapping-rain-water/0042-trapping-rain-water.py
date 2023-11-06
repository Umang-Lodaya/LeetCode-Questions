class Solution:
    def trap(self, height: List[int]) -> int:
        leftMax, rightMax = [-float("inf")] * 2
        left = 0; right = len(height) - 1
        trappedWater = 0
        while left < right:
            leftMax = max(leftMax, height[left])
            rightMax = max(rightMax, height[right])
            
            if height[left] < height[right]:
                trappedWater -= height[left] - leftMax
                left += 1
            else:
                trappedWater -= height[right] - rightMax
                right -= 1
        
        return trappedWater