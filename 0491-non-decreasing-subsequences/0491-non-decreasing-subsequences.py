class Solution:
    def solve(self, nums, index, output, ans):
        if index >= len(nums):
            if len(output) > 1:
                ans.add(tuple(output))
            return
        
        if not output or nums[index] >= output[-1]:
            output.append(nums[index])
            self.solve(nums, index+1, output, ans)
            output.pop()
        
        self.solve(nums, index+1, output, ans)

    def findSubsequences(self, nums: List[int]) -> List[List[int]]:
        ans = set()
        self.solve(nums, 0, [], ans)
        return [list(x) for x in ans]