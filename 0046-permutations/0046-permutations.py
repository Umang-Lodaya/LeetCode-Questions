class Solution:
    def permute(self, nums):
        res = []
        self.dfs(nums, [], res)
        return res

    def dfs(self, num, path, res):
        if not num:
            res.append(path)
        else:
            for i in range(len(num)):
                self.dfs(num[:i]+num[i+1:], path+[num[i]], res)