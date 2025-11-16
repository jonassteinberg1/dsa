from typing import Optional

class Node:
    def __init__(self, val, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

class Solution:
    def treeToDoublyList(self, root: 'Node') -> 'Node':
        stack = []
        head = prev = None
        curr = root
        
        while stack or curr:
            while curr:
                stack.append(curr)
                curr = curr.left
            node = stack.pop()
            if prev:
                prev.right = node
                node.left = prev
            else:
                head = node
            
            if node.right:
                stack.append(node.right)

            prev = node
        
        head.left = prev
        prev.right = head



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