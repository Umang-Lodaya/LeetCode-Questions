class Solution:
    def minDepth(self, root: Optional[TreeNode]) -> int:
        if root is None:
            return 0

        left_height = self.minDepth(root.left)
        right_height = self.minDepth(root.right)

        if left_height == 0:
            return right_height + 1

        if right_height == 0:
            return left_height + 1

        return min(right_height , left_height) + 1