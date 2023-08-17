# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def pathSum(self, root: Optional[TreeNode], targetSum: int) -> List[List[int]]:
        def dfs(node, target, path):
            if not node: return None
            path.append(node.val)
            target -= node.val
            
            if not node.left and not node.right:
                if target == 0:
                    ans.append(path.copy())
            else:
                dfs(node.left, target, path)
                dfs(node.right, target, path)
            path.pop()
            
        ans = []
        dfs(root, targetSum, [])
        return ans