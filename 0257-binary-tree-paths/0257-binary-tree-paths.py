# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def binaryTreePaths(self, root: Optional[TreeNode]) -> List[str]:
        def dfs(node, path):
            if not node: return None
            path.append(str(node.val))
            
            if not node.left and not node.right:
                ans.append(path.copy())
            else:
                dfs(node.left, path)
                dfs(node.right, path)
                
            path.pop()
        
        ans = []
        dfs(root, [])
        
        for i in range(len(ans)):
            path = ans[i]
            path = '->'.join(path)
            ans[i] = path
            
        return ans