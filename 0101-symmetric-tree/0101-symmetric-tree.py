# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def isSymmetric(self, root: Optional[TreeNode]) -> bool:
        return self.isSameTreeReverse(root.left, root.right)

    def isSameTreeReverse(self, p, q):
        if p is None and q is None:
            return True

        if p and q and p.val == q.val:
            return self.isSameTreeReverse(p.left, q.right) and self.isSameTreeReverse(p.right, q.left)

        return False