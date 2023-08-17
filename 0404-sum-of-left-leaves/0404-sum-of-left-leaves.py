# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def sumOfLeftLeaves(self, root: Optional[TreeNode]) -> int:
        ans = 0
        def dfs(node, left = False):
            nonlocal ans
            if not node: return None
            dfs(node.left, True)
            if not node.left and not node.right and left == True:
                ans += node.val

            dfs(node.right)
        
        # ans = 0
        dfs(root)
        return ans