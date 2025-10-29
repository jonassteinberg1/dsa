class Node:
    def __init__(self, val):
        self.val = val
        self.left = None
        self.right = None
        self.parent = None

class Solution:
    def lowestCommonAncestor(self, p: Node, q: Node) -> Node:
        if p is q:
            return p
        self.lowestCommonAncestor(p.parent, q.parent)
        

n1 = Node(1)
n2 = Node(2)
n3 = Node(3)
n4 = Node(4)


n1.left = n2
n2.parent = n1
n2.left = n3
n3.parent = n2
n2.right = n4
n4.parent = n2

Solution().lowestCommonAncestor(n3, n4)