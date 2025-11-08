from typing import Optional

class TreeNode:
    def __init__(self, val: int = 0, left: 'Optional[TreeNode]' = None, right: 'Optional[TreeNode]' = None):
        self.val = val
        self.left = left
        self.right = right

class Solution:
    def lcaTwoOfThree(self, root: Optional[TreeNode], a: int, b: int, c: int) -> Optional[TreeNode]:
        if root is None:
            return None
        if root is a:
            return 1
        if root is b:
            return 1
        if root is c:
            return 1
        
        t1 = self.lcaTwoOfThree(root.left, a, b, c)
        t2 = self.lcaTwoOfThree(root.right, a, b, c)

n1 = TreeNode(1)
n2 = TreeNode(2)
n3 = TreeNode(3)

n1.left = n2
n1.right = n3
        
