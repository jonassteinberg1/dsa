
from typing import Optional

class Node:
    def __init__(self, val, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

class Solution:
    def treeToDoublyList(self, root: 'Node') -> 'Node':
        stack = [] # iterative tree
        head = prev = None # 
        curr = root # have to start somewhere

        if not root:
            return root
        
        while stack or curr:
            if curr:
                stack.append(curr)
                curr = curr.left
            else:
                node = stack.pop()
                if prev:
                    prev.right = node
                    node.left = prev
                else:
                    head = node
                prev = node
                curr = node.right
        
        head.left = prev
        prev.right = head

        return head



n4 = Node(4)
n2 = Node(2)
n1 = Node(1)
n3 = Node(3)
n5 = Node(5)

n4.left = n2
n2.left = n1
n2.right = n3
n4.right = n5

s = Solution()
s.treeToDoublyList(n4)