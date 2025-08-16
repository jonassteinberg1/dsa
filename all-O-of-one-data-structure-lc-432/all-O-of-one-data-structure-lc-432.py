class Node:
    def __init__(self, key: str):
        self.key = key
        self.next = None
        self.prev = None

class AllOne:

    def __init__(self):
        self.strings = {}
        self.head = Node('string1')
        self.tail = Node('string2')
        self.head.next = self.tail
        self.tail.prev = self.head

    def inc(self, key: str) -> None:
        if key in self.strings:
            self.strings[key] += 1
        else:
            node = Node(key)
            
            self.strings[key] = 1

    def dec(self, key: str) -> None:
        count = self.strings[key]
        if (count - 1) == 0:
            del self.strings[key]
        else:
            self.strings[key] -= 1          

    def getMaxKey(self) -> str:
        

    def getMinKey(self) -> str:
        


# ["AllOne","inc","inc","getMaxKey","getMinKey","inc","getMaxKey","getMinKey"]
# [[],["hello"],["hello"],[],[],["leet"],[],[]]