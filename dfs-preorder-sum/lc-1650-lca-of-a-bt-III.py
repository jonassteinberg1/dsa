class Node:
    def __init__(self, val: int, left: int, right: int):
        self.val = val
        self.left = left
        self.right = right

class RecursiveSum:
    def __init__(self):
        pass
    
    def return_sum(self, node: Node):
        if node is None: 
            return 0
        print("enter", node.val)
        return node.val + self.return_sum(node.left) + self.return_sum(node.right)
        print("exit", node.val)
    
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

r = RecursiveSum()
print(r.return_sum(n1))

# pick up analyzing how it seems like self.return_sum(node.right) is called "at the same time" as node.val + self.return_sum(node.left)