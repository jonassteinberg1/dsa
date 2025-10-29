class Node:
    def __init__(self, val):
        self.val = val
        self.left = None
        self.right = None
        self.parent = None

class Solution:
    def lowestCommonAncestor(self, p: Node, q: Node) -> Node:
        if p is q.parent:
            return p.val
        self.lowestCommonAncestor(p, q.parent)
        

n1 = Node(1)
n2 = Node(2)
n3 = Node(3)
n4 = Node(4)

n1.right = n3
n1.left = n2
n2.parent = n1
n3.parent = n1
n2.left = n4
n4.parent = n2

Solution().lowestCommonAncestor(n4, n3)