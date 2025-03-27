from typing import Optional

# Definition for singly-linked node.
#class ListNode:
#    def __init__(self, val=0, next=None):
#        self.val = val
#        self.next = next

class Solution:
    def mergeTwoLists(self, node1: Optional[Node], node2: Optional[Node]) -> Optional[Node]:
        head = None
        if node1 is None:
            return node2
        if node2 is None:
            return node1
        
        if node1.val <= node2.val:
            head = node1
        else:
            head = node2

        while node1 or node2:
            if node1 is None:
                return node2
            if node2 is None:
                return node1
            if node1.val <= node2.val:
                while node1 and node1.next and node1.next.val <= node2.val:
                    # visit the next linked node
                    node1 = node1.next
                node1.next = node2
                node2 = node2.next
            else:
                while node2 and node2.next and node2.next.val <= node1.val:
                    node2 = node2.next
                node2.next = node1
                node1 = node1.next
        return head
    
    