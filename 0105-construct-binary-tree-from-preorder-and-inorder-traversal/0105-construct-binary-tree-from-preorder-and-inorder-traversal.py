# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def buildTree(self, preorder: List[int], inorder: List[int]) -> Optional[TreeNode]:
        MAP = {inorder[i]: i for i in range(len(inorder))}

        def buildTreePartition(preStart,preEnd,inStart,inEnd):
            if preStart > preEnd or inStart > inEnd:
                return None
            
            root = TreeNode(preorder[preStart])
            inRoot = MAP[root.val]
            numsLeft = inRoot - inStart

            root.left = buildTreePartition(preStart + 1, preStart + numsLeft, inStart, inRoot - 1)
            root.right = buildTreePartition(preStart + numsLeft + 1, preEnd, inRoot + 1, inEnd)

            return root

        return buildTreePartition(0, len(preorder) - 1, 0, len(inorder) - 1)