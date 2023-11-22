class Solution:
    def findDiagonalOrder(self, nums: List[List[int]]) -> List[int]:
        res = defaultdict(list)
        for i, row in enumerate(nums):
            for j, x in enumerate(row):
                res[i + j].insert(0, x)
                
        return chain(*res.values())