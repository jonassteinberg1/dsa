from typing import Optional

class Node:
    def __init__(self, val):
        self.val = val
        self.left = None
        self.right = None

class LcaIfPresent:
    def lcaIfPresent(self, root: Node, p: Node, q: Node):
        # base cases
        if root is None:
            return None, False, False
        if root is p:
            return root, True, False
        if root is q:
            return root, False, True
        
        # postorder
        left, l_sp, r_sp = self.lcaIfPresent(root.left, p, q)
        right, l_sq, r_sq = self.lcaIfPresent(root.right, p, q)
        
        # postorder logic: tracking
        seen_p_here = l_sp or r_sp or (root is p)
        seen_q_here = l_sq or r_sq or (root is q)

        # postorder logic: combine step
        if left is not None and right is not None:
            cand = root
        elif left is not None:
            cand = left
        elif right is not None:
            cand = right
        else:
            cand = None
        
        return cand, seen_p_here, seen_q_here
        
        

# nodes
n3 = Node(3); n5 = Node(5); n1 = Node(1)
n6 = Node(6); n2 = Node(2); n0 = Node(0)
n8 = Node(8); n7 = Node(7); n4 = Node(4)
n42 = Node(42)

# links (n3 is the root)
n3.left, n3.right = n5, n1
n5.left, n5.right = n6, n2
n1.left, n1.right = n0, n8
n2.left, n2.right = n7, n4

lca = None

s = LcaIfPresent()
try:
    assert s.lcaIfPresent(n3, n5, n42) == lca
    print(f"lac is {lca.x}")
except AssertionError:
    print("incorrect ancestor")