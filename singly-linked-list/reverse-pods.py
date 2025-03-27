class LinkedList:

    def __init__(self):
        self.head = None

    def append(self, pod_id):
        if not self.head:
            self.head = Node(pod_id)
            
        else:
            current = self.head
            while current.next is not None:
                current = current.next
            current.next = Node(pod_id)
        
    def reverse(self):
        current = self.head
        prev = None
        while current is not None:
            next_node = current.next
            current.next = prev
            prev = current
            current = next_node
        self.head = prev        
            
class Node:
    def __init__(self, pod_id: str, next=None):
        self.pod_id = pod_id
        self.next = next

l = LinkedList()
l.append(1)
l.append(2)
l.append(3)
l.append(4)
l.reverse()

