class Node:
    def __init__(self, val: int, left: int, right: int):
        self.val = val
        self.left = left
        self.right = right

class RecursiveSum:
    def __init__(self) -> int:
        self.tree_sum = 0
    
    def return_sum(self, node: Node):
        if node.left is None and node.right is None:
            self.tree_sum += node.val
        elif node.left:
            self.return_sum(node.left)
            if node.right:
                self.return_sum(node.right)
            self.tree_sum += node.val
        else:
            self.return_sum(node.right)
            if node.left:
                self.return_sum(node.left)
            self.tree_sum += node.val
        return self.tree_sum
    

n4 = Node(4, None, None)
n3 = Node(3, None, None)
n2 = Node(2, n4, None)
n1 = Node(1, n2, n3)

r = RecursiveSum()
print(r.return_sum(n1))