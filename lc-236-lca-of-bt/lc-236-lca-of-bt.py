class TreeNode:
    def __init__(self, x):
        self.x = x
        self.left = None
        self.right = None

class Solution:
    def lowestCommonAncestor(self, root: 'TreeNode', p: 'TreeNode', q: 'TreeNode') -> 'TreeNode':
        if root is None:
            return None
        if root is p or root is q:
            return root
        left = self.lowestCommonAncestor(root.left, p, q)
        right = self.lowestCommonAncestor(root.right, p, q)
        if left is not None and right is not None:
            return root
        elif left is not None:
            return left
        elif right is not None:
            return right
        else:
            return None
        
        
        

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

#n0 = TreeNode(0)
#n1 = TreeNode(1)
#n2 = TreeNode(2)
#n3 = TreeNode(3)
#n4 = TreeNode(4)
#n0.left = n1
#n1.left = n3
#n0.right = n2
#n2.right = n4

#n0 = TreeNode(0)
#n1 = TreeNode(1)
#n2 = TreeNode(2)
#n0.left = n1
#n1.left = n2

#n1 = TreeNode(1)
#n2 = TreeNode(2)
#n3 = TreeNode(3)
#n4 = TreeNode(4)
#n5 = TreeNode(5)
#n6 = TreeNode(6)
#n7 = TreeNode(7)
#n8 = TreeNode(8)
#n9 = TreeNode(9)
#n10 = TreeNode(10)

#n1.left = n2
#n2.left = n3
#n3.left = n4
#n2.right = n5
#n5.right = n10
#n5.left = n6
#n6.left = n7
#n7.left = n8
#n7.right = n9

n1 = TreeNode(1)
n2 = TreeNode(2)
n3 = TreeNode(3)
n4 = TreeNode(4)
n5 = TreeNode(5)
n6 = TreeNode(6)
n7 = TreeNode(7)
n1.left = n2
n2.left = n4
n4.left = n6
n1.right = n3
n3.right = n5
n5.right = n7

#n1 = TreeNode(1); n2 = TreeNode(2); n3 = TreeNode(3); n4 = TreeNode(4)
#n1.left = n2
#n1.right = n3
#n2.left = n4

lca = n1

s = Solution()
#s.lowestCommonAncestor(n3, n5, n1)
try:
    assert s.lowestCommonAncestor(n1, n6, n7) == lca
    print(f"lac is {lca.x}")
except AssertionError:
    print("incorrect ancestor")
#s.lowestCommonAncestor(n0, n1, n2)