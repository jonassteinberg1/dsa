class Node:
    def __init__(self, val):
        self.val = val
        self.left = None
        self.right = None
        self.parent = None

class Solution:
    def lowestCommonAncestor(self, p: Node, q: Node) -> Node:
        p_start = p
        q_start = q
        if not p.parent:
            return p
        if not q.parent:
            return q
        while p and q:
            if p is q:
                return p
            elif p.parent and q.parent:
                p = p.parent
                q = q.parent
            elif not p.parent:
                p = q_start
            else:
                q = p_start


n1 = Node(1)
n2 = Node(2)
n3 = Node(3)
n4 = Node(4)
n1.left = n2
n1.right = n3
n2.left = n4
n2.parent = n1
n3.parent = n1
n4.parent = n2

#n1 = Node(1)
#n2 = Node(2)
#n1.left = n2
#n2.parent = n1


Solution().lowestCommonAncestor(n4, n1)