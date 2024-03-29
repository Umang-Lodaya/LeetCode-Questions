class Solution:
    def findMode(self, root: Optional[TreeNode]) -> List[int]:
        def dfs(node, freq):
            freq[node.val] = freq.get(node.val, 0) + 1
            if node.left: dfs(node.left, freq)
            if node.right: dfs(node.right, freq)
        
        freq = {}
        dfs(root, freq)
        
        k = sorted(freq.items(), key = lambda x:x[1], reverse = True)
        k = list(filter(lambda x:x[1] == k[0][1], k))
        
        return [i[0] for i in k]