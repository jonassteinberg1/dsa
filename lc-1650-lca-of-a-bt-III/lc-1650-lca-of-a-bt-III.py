class Node:
    def __init__(self, val, left=None, right=None):
        self.val, self.left, self.right = val, left, right

def tree_sum(node):
    if node is None:
        print("return 0  ← base")
        return 0
    print(f"enter {node.val}")
    left  = tree_sum(node.left)
    print(f"back to {node.val} after LEFT")
    right = tree_sum(node.right)
    total = node.val + left + right
    print(f"return {total} from {node.val}  (left={left}, right={right})")
    return total

# Tree:
#     1
#    / \
#   2   3
#  / \
# 4   5
n4 = Node(4)
n5 = Node(5)
n2 = Node(2, n4, n5)
n3 = Node(3)
n1 = Node(1, n2, n3)

tree_sum(n1)