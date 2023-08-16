class Solution(object):
    def isBalanced(self, root):
        return (self.Height(root) >= 0)
    
    def Height(self, root):
        if not root:  
            return 0
        
        leftHeight, rightHeight = self.Height(root.left), self.Height(root.right)
        
        if leftHeight < 0 or rightHeight < 0 or abs(leftHeight - rightHeight) > 1:  
            return -1
        
        return max(leftHeight, rightHeight) + 1