from typing import Optional

class Node:
    def __init__(self, val, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

class Solution:
    def treeToDoublyList(self, root: 'Node') -> 'Node':
        # empty list
        if root is None:
            return None

        def dfs(node: 'Node'):
            if node is None:
                return (None, None)

            # Inorder: process left
            Lh, Lt = dfs(node.left)

            # Link predecessor (left tail) <-> node, decide head
            if Lt:
                Lt.right = node
                node.left = Lt
                head = Lh
            else:
                node.left = None
                head = node

            # Then process right
            Rh, Rt = dfs(node.right)

            # Link node <-> successor (right head), decide tail
            if Rh:
                node.right = Rh
                Rh.left = node
                tail = Rt
            else:
                node.right = None
                tail = node

            return (head, tail)

        head, tail = dfs(root)
        # Close the list to make it circular
        head.left = tail
        tail.right = head
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


#       n4
#      /  \
#    n2    n5
#   /  \
# n1    n3


s = Solution()
s.treeToDoublyList(n4)