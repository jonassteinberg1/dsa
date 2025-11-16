class Node:
    def __init__(self, val: int):
        self.val = val
        self.left = None
        self.right = None

class BstToDll:
    def bst_to_dll(self, root: Node):
        stack = []
        head = prev = None
        curr = root
        stack.append(curr)

        if not root:
            return root

        while stack or curr:
            if curr.left:
                curr = curr.left
                stack.append(curr)
            else:
                node = stack.pop
                if prev:
                    node.left = prev
                    prev.right = node
                else:
                    head = curr
                
                prev = curr
                curr = node.right
        
        return (head, prev)
    
