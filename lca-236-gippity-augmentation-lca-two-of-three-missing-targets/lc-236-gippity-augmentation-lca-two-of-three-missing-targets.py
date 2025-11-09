

### UNFINISHED SOLUTION ###

from typing import Optional

class TreeNode:
    def __init__(self, val: int = 0, left: 'Optional[TreeNode]' = None, right: 'Optional[TreeNode]' = None):
        self.val = val
        self.left = left
        self.right = right

class Solution:
    def lcaTwoOfThree(self, root: Optional[TreeNode], a: TreeNode, b: TreeNode, c: TreeNode) -> Optional[TreeNode]:
        # base case
        if root is None:
            return None, False, False, False
        
        # postorder
        l_lca, la, lb, lc = self.lcaTwoOfThree(root.left, a, b, c)
        r_lca, ra, rb, rc = self.lcaTwoOfThree(root.right, a, b, c)
        
        # postorder logic: combine step
        seen_a = la or ra or (root is a)
        seen_b = lb or rb or (root is b)
        seen_c = lc or rc or (root is c)

        if seen_a + seen_b + seen_c >= 2:
            return root, seen_a, seen_b, seen_c
        else:
            return None, seen_a, seen_b, seen_c

        




n1 = TreeNode(1)
n2 = TreeNode(2)
n3 = TreeNode(3)
n4 = TreeNode(4)
n5 = TreeNode(5)
n6 = TreeNode(6)
n7 = TreeNode(7)

n1.left = n2
n2.left = n3
n1.right = n4
n4.left = n5
n4.right = n7
n5.left = n6

lca = n4, True, True, True

s = Solution()

try:
    assert s.lcaTwoOfThree(n1, n3, n5, n7) == lca
    print(f"lac is {lca.x}")
except AssertionError:
    print("incorrect ancestor")
        
