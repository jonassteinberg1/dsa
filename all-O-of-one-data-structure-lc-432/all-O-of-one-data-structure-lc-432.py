class Node:
    def __init__(self, key):
        self.key = key
        self.prev, self.next = None

class AllOne:
    def __init__(self):
        self.strings = {}
        self.head = Node('string') # initialize doubly linked list
        self.tail = Node('string')
        self.head.next = self.tail # initialize head and tail
        self.tail.prev = self.head

    def inc(self, key: str) -> None:
        if key not in self.strings:
            node = Node(key)
            self.strings[key] = [1, node]
        else:
            self.strings[key][0] += 1
            if self.strings[key][0]

    def dec(self, key: str) -> None:
        if self.strings[key][0] == 1:
            node = self.strings[key][1]
            self.remove(node)
            del self.strings[key]
        else:
            self.strings[key][0] -= 1

    def getMaxKey(self) -> str:
        if key not in self.strings:
            return ""
        return self.tail

    def getMinKey(self) -> str:
        if key not in self.strings:
            return ""
        return self.head
        
    def remove(self, node):
        node.prev.next = node.next
        node.next.prev = node.prev
