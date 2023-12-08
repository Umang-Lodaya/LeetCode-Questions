class Solution:
    def tree2str(self, root):
        if root is None:
            return ""

        result = str(root.val)

        left_subtree = self.tree2str(root.left)
        right_subtree = self.tree2str(root.right)

        if not left_subtree and not right_subtree:
            return result
        if not left_subtree:
            return result + "()" + "(" + right_subtree + ")"
        if not right_subtree:
            return result + "(" + left_subtree + ")"

        return result + "(" + left_subtree + ")" + "(" + right_subtree + ")"