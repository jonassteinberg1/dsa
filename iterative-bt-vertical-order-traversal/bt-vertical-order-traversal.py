# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

from collections import deque, defaultdict
from typing import Optional, List

class Solution:
    def verticalOrder(self, root: Optional[TreeNode]) -> List[List[int]]:
        if 

        d = deque()
        hd = 0
        order = defaultdict(list)

        d.append((root, hd))

        while len(d) > 0:
            process = d.popleft()
            order[process[1]].append(process[0].val)
            if process[0].left:
                d.append((process[0].left, process[1] - 1))
            if process[0].right:
                d.append((process[0].right, process[1] + 1))
            
        vertical = [order[el] for el in sorted(order)]
        return vertical
    

root = TreeNode(1)
root.left = TreeNode(2)
root.right = TreeNode(3)
root.left.left = TreeNode(4)
root.right.right = TreeNode(5)
root.left.right = TreeNode(6)
root.right.left = TreeNode(7)

s = Solution()
s.verticalOrder(root)