class Node:
    def __init__(self, key):
        self.key = key
        self.val = 1
        self.prev = None
        self.next = None

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
            self.add_to_head(node)
            self.strings[key] = node
        else:
            node = self.strings[key]
            if (self.strings[key].val + 1) >= self.tail.prev.val:
                self.remove(node)
                self.add_to_tail(node)
                self.strings[key].val += 1
            elif (self.strings[key].val + 1) >= self.head.next.val and len(self.strings) == 2:
                self.strings[key].val += 1
            elif (self.strings[key].val + 1) >= self.head.next.val:
                self.remove(node)
                self.next_head_swap(node)
                self.strings[key].val += 1
            else:
                self.strings[key].val += 1
            
    def dec(self, key: str) -> None:
        node = self.strings[key]
        if (self.strings[key].val - 1) == 0:
            self.remove(node)
            del self.strings[key]
        elif (self.strings[key].val - 1) <= self.head.next.val:
            self.remove(node)
            self.add_to_head(node)
            self.strings[key].val -= 1
        elif (self.strings[key].val - 1) >= self.tail.prev.val:
            self.remove(node)
            self.add_to_tail(node)
            self.strings[key].val -= 1
        elif (self.strings[key].val - 1) < self.tail.prev.val:
            self.remove(node)
            self.next_tail_swap(node)
            self.strings[key].val -= 1
        elif (self.strings[key].val - 1) > self.head.next.val and (self.strings[key].val - 1) <= self.head.next.next.val:
            self.remove(node)
            n1 = self.head.next.next
            self.head.next.next = node
            node.prev = self.head.next
            node.next = n1.prev
            self.strings[key].val -= 1
        else:
            self.strings[key].val -= 1
    

    def getMaxKey(self) -> str:
        if len(self.strings) == 0:
            return ""
        return self.tail.prev.key

    def getMinKey(self) -> str:
        if len(self.strings) == 0:
            return ""
        return self.head.next.key
        
    def remove(self, node):
        node.prev.next = node.next
        node.next.prev = node.prev
    
    def add_to_tail(self, node):
        prev = self.tail.prev
        self.tail.prev = node
        node.next = self.tail
        prev.next = node
        node.prev = prev

    def add_to_head(self, node):
        nex = self.head.next
        self.head.next = node
        nex.prev = node
        node.prev = self.head 
        node.next = nex
    
    def next_head_swap(self, node):
        n1 = self.head.next
        n2 = n1.next
        n1.next = node
        node.prev = n1
        node.next = n2
        n2.prev = node
    
    def next_tail_swap(self, node):
        n1 = self.tail.prev
        n2 = n1.prev
        n1.prev = node
        node.next = n1
        node.prev = n2
        n2.next = node


def run(arr: list):
    l = []
    ao = AllOne()
    l.append('null')
    for el in arr[1:]:
        if el[0] == "getMinKey":
            min = ao.getMinKey()
            l.append(min)
        elif el[0] == "getMaxKey":
            max = ao.getMaxKey()
            l.append(max)
        elif el[0] == "inc":
            ao.inc(el[1][0])
            l.append('null')
        else:
            ao.dec(el[1][0])
            l.append('null')
    return l

# expected
# 

run([('AllOne', []),
 ('inc', ['hello']),
 ('inc', ['l']),
 ('inc', ['l']),
 ('inc', ['l']),
 ('inc', ['k']),
 ('inc', ['k']),
 ('inc', ['k']),
 ('inc', ['j']),
 ('inc', ['j']),
 ('inc', ['j']),
 ('dec', ['j']),
 ('dec', ['k']),
 ('getMaxKey', [])])