class Node:
    def __init__(self, key, val):
        self.key = key
        self.val = val
        self.prev = None
        self.next = None

class LRUCache:
    def __init__(self, capacity):
        self.capacity = capacity
        self.tracker = {}
        self.head = Node(0, 0)
        self.tail = Node(0, 0)
        self.head.next = self.tail
        self.tail.prev = self.head

    def get(self, key):
        if key not in self.tracker:
            return -1
        self.remove(key)
        node = self.tracker[key]
        self.add_to_tail(node)
        return node.val
    
    def put(self, key, val):
        if key in self.tracker:
            self.remove(key)
            del self.tracker[key]
        node = Node(key, val)
        self.add_to_tail(node)
        self.tracker[key] = node
        if len(self.tracker) > self.capacity:
            head_next_key = self.head.next.key
            self.remove(head_next_key)
            del self.tracker[head_next_key]

    def remove(self, key):
        node = self.tracker[key]
        node.prev.next = node.next
        node.next.prev = node.prev
    
    def add_to_tail(self, node):
        prev = self.tail.prev
        self.tail.prev = node
        node.next = self.tail
        node.prev = prev
        prev.next = node


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

run([[2],[1,1],[2,2],[1],[3,3],[2],[4,4],[1],[3],[4]])
