class Node:
    def __init__(self, val: int, left: int, right: int):
        self.val = val
        self.left = left
        self.right = right

class RecursiveDfsInOrderSum:
    def __init__(self):
        self.tree_sum = 0
    
    def inorder(self, node: Node):
        if node is None:
            return 0
        else:
            self.inorder(node.left)
            self.tree_sum += node.val
            self.inorder(node.right)
        return self.tree_sum
    
n15 = Node(15, None, None)
n14 = Node(14, None, None)
n13 = Node(13, None, n15)
n12 = Node(12, n14, None)
n11 = Node(11, None, None)
n10 = Node(10, n12, n13)
n9 = Node(9, n10, None)
n8 = Node(8, n11, n9)
n7 = Node(7, None, None)
n6 = Node(6, n7, n8)
n5 = Node(5, None, None)
n4 = Node(4, n5, n6)
n3 = Node(3, None, n4)
n2 = Node(2, n3, None)
n1 = Node(1, n2, None)  # root

r = RecursiveDfsInOrderSum()
print(r.inorder(n1))

# pick up analyzing how it seems like self.return_sum(node.right) is called "at the same time" as node.val + self.return_sum(node.left)