#User function Template for python3

class Solution:
    ans = -1
    def floor(self, root, x):
        if not root:
            return -1
        
        if root.data == x:
            return x
        
        if root.data < x:
            self.ans = max(self.ans, root.data)
            self.ans = max(self.ans, self.floor(root.right, x))
            return self.ans
        
        self.ans = max(self.ans, self.floor(root.left, x))
        return self.ans


#{ 
 # Driver Code Starts
#Initial Template for Python 3

class Node:
    def __init__(self, val):
        self.right = None
        self.data = val
        self.left = None

def insert(tree, val):
    if(tree==None):
        return Node(val)
    if(val< tree.data):
        tree.left= insert(tree.left, val)
    elif(val > tree.data):
        tree.right= insert(tree.right, val)
    return tree
    
if __name__=="__main__":
    t=int(input())
    for _ in range(0,t):
        n=int(input())
        arr= list(map(int, input().split()))
        root = None
        for k in arr:
            root=insert(root, k)
        s=int(input())
        obj = Solution()
        print(obj.floor(root,s))
# } Driver Code Ends