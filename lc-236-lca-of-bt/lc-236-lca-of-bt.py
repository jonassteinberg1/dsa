class TreeNode:
    def __init__(self, x):
        self.x = x
        self.left = None
        self.right = None

class Solution:
    def lowestCommonAncestor(self, root: 'TreeNode', p: 'TreeNode', q: 'TreeNode') -> 'TreeNode':
        r0 = root
        if root is q and root is q:
            return r0
        self.lowestCommonAncestor(root.left, p, q)
        self.lowestCommonAncestor(root.right, p, q)
        

#n3 = TreeNode(3)
#n5 = TreeNode(5)
#n1 = TreeNode(1)
#n6 = TreeNode(6)
#n2 = TreeNode(2)
#n7 = TreeNode(7)
#n4 = TreeNode(4)
#n0 = TreeNode(0)
#n8 = TreeNode(8)

#n3.left = n5
#n3.right = n1
#n5.left = n6
#n5.right = n2
#n2.left = n7
#n2.right = n4
#n1.left = n0
#n1.right = n8

n0 = TreeNode(0)
n1 = TreeNode(1)
n2 = TreeNode(2)
n3 = TreeNode(3)
n4 = TreeNode(4)
n0.left = n1
n1.left = n3
n0.right = n2
n2.right = n4

s = Solution()
#s.lowestCommonAncestor(n3, n5, n1)
s.lowestCommonAncestor(n0, n3, n4)