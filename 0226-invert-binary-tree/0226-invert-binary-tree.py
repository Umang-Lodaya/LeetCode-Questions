class Solution(object):
    def invertTree(self, root):
        # Base case...
        if root == None:
            return root
        
        root.left, root.right = root.right, root.left
        
        self.invertTree(root.left)
        
        self.invertTree(root.right)
        
        return root