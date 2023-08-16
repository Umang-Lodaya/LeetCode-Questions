# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def maxPathSum(self, root: Optional[TreeNode]) -> int:
        pathSum = -float('inf')
        
        def height(root):
            nonlocal pathSum
            if not root:
                return 0
            
            l = max(0, height(root.left))
            r = max(0, height(root.right))
            
            pathSum = max(pathSum, l + r + root.val)
            
            return root.val + max(l, r)
        
        height(root)
        return pathSum