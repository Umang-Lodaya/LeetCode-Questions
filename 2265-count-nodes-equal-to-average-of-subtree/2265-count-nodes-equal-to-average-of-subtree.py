# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def averageOfSubtree(self, root: Optional[TreeNode]) -> int:
        if not root.left and not root.right:
            return 1
        
        result = 0
        
        def dfs(node):
            nonlocal result
            if not node:
                return [0, 0]
            
            lSum, lCount = 0, 0
            lSum, lCount = dfs(node.left)
            
            rSum, rCount = 0, 0
            rSum, rCount = dfs(node.right)
            
            s = lSum + rSum + node.val
            c = lCount + rCount + 1
            avg = s // c
            
            if avg == node.val:
                result += 1
            
            return [s, c]
        
        total, count = dfs(root)
        return result