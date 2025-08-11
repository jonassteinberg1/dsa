class Node:
    def __init__(self, k, v):
        self.key = k
        self.val = v
        self.prev = None
        self.next = None

class LRUCache:
    def __init__(self, capacity):
        self.capacity = capacity
        self.dic = dict()
        self.head = Node(0, 0)
        self.tail = Node(0, 0)
        self.head.next = self.tail
        self.tail.prev = self.head

    def get(self, key):
        if key in self.dic:
            n = self.dic[key]
            self.remove(n)
            self.add(n)
            return n.val
        return -1

    def put(self, key, value):
        if key in self.dic:
            self.remove(self.dic[key])
        n = Node(key, value)
        self.add(n)
        self.dic[key] = n
        if len(self.dic) > self.capacity:
            n = self.head.next
            self.remove(n)
            del self.dic[n.key]

    def remove(self, node):
        p = node.prev
        n = node.next
        p.next = n
        n.prev = p

    def add(self, node):
        p = self.tail.prev
        p.next = node
        self.tail.prev = node
        node.prev = p
        node.next = self.tail     


    def check(self, d: dict, h: Node, t: Node):
        self.d = d
        self.h = h
        self.t = t
        k = list(self.d.keys())
        v = list(self.d.values())
        for idx, val in enumerate(k):
            if len(k) == 1:
                assert self.h is self.t
                assert v[idx] is self.h
                assert v[idx] is self.t
                assert v[idx].prev_node is None
                assert v[idx].next_node is None
            elif v[idx] is self.h:
                assert v[idx].prev_node is None
                assert v[idx].next_node is v[idx+1]
            elif v[idx] is self.t:
                assert v[idx].prev_node is v[idx-1]
                assert v[idx].next_node is None
            else:
                assert v[idx].next_node is v[idx+1]
                assert v[idx].prev_node is v[idx-1]

# at least to dupe [6]
def run(arr: list):
    l = []
    lru = LRUCache(arr[0][0])
    l.append(['null'])
    for el in arr[1:]:
        if len(el) == 1:
            l.append(lru.get(el[0]))
        else:
            l.append(lru.put(el[0], el[1]))
    return l

run([[1],[2,1],[2],[3,2],[2],[3]])
