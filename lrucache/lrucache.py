# TO DO
# take it from the top of put() and notes

from typing import Any

class Node:
    def __init__(self, key: int, val: int):
        self.key = key
        self.val = val
        self.next_node: Node | None = None
        self.prev_node: Node | None = None

class LRUCache:

    def __init__(self, capacity: int):
        self.capacity = capacity
        self.tracker = {}
        self.head: Node | None = None
        self.tail: Node | None = None

    def get(self, key: int) -> int:
        node = self.tracker.get(key)
        # head switch
        if node:
            # size of 1 "switch"
            if not node.prev_node and not node.next_node:
                self.check(self.tracker, self.head, self.tail)
                return [node.val]
            # head switch
            elif not node.prev_node:
                node.next_node.prev_node = None # make next node's (head) prev_node None
                self.head = node.next_node
                self.remove(key)
                self.add(node)
                self.check(self.tracker, self.head, self.tail)
                return [node.val]
            # tail switch
            elif not node.next_node:
                self.check(self.tracker, self.head, self.tail)
                return [node.val]
            # normal switch
            else:
                node.prev_node.next_node = node.next_node
                node.next_node.prev_node = node.prev_node
                self.remove(key)
                self.add(node)
                self.check(self.tracker, self.head, self.tail)
                return [node.val]
        else:
            self.check(self.tracker, self.head, self.tail)
            return [-1]

    def put(self, key: int, val: int) -> None:
        # check the len 0 case
        if self.head:
            # begin checking the cases where len more than 0
            # we start with len 1 and at capacity
            #if len(self.tracker.keys()) == 1 and key in self.tracker:
            if len(self.tracker.keys()) == 1 and (self.capacity == 1 or key in self.tracker):
                self.remove(self.head.key)
                self.tracker[key] = Node(key, val)
                self.head = self.tracker[key]
                self.tail = self.tracker[key]
            # len 1 and not at capacity
            elif len(self.tracker.keys()) == 1:
                self.add(Node(key, val))
                self.head = self.tail.prev_node
                self.head.prev_node = None
            # len 2 and matching head
            # note: match implies capacity is not met because
            # the match has to be removed
            elif len(self.tracker.keys()) >= 2 and self.head.key == key:
                self.remove(key)
                self.add(Node(key, val))
                self.head = self.head.next_node
                self.head.prev_node = None
            # len 2 and matching tail
            elif len(self.tracker.keys()) == 2 and self.tail.key == key:
                self.remove(key)
                node = Node(key, val)
                self.tail = node
                self.head.next_node = node
                self.tail.prev_node = self.head
                self.tracker[key] = node
            elif len(self.tracker.keys()) == 2 and self.capacity == 2:
                self.remove(self.head.key)
                self.add(Node(key, val))
                self.head = self.tail.prev_node
                self.head.prev_node = None
            elif len(self.tracker.keys()) > 2 and self.tail.key == key:
                self.remove(key)
                node = Node(key, val)
                prev_tail = self.tail
                self.tail = node
                node.prev_node = prev_tail.prev_node
                prev_tail.prev_node.next_node = node
                self.tracker[key] = node
            # len 2 or more matching but not head nor tail
            elif len(self.tracker.keys()) >= 2 and key in self.tracker:
                node = self.tracker[key]
                node.prev_node.next_node = node.next_node
                node.next_node.prev_node = node.prev_node
                self.remove(key) # [11] at least
                self.add(Node(key, val))
            # implicitly by the cases above len 2 or more and at capacity
            elif len(self.tracker.keys()) == self.capacity:
                self.remove(self.head.key)
                self.add(Node(key, val))
                self.head = self.head.next_node
                self.head.prev_node = None
            # len 2 or more not at capacity no match
            else:
                self.add(Node(key, val))
        else:
            # len 0
            self.tracker[key] = Node(key, val)
            self.head = self.tracker[key]
            self.tail = self.tracker[key]
        self.check(self.tracker, self.head, self.tail)
        return ['null']

    def remove(self, key: int) -> None:
        try: # because they could try a get for a key not present
            del self.tracker[key]
        except KeyError as e:
            return
    
    def add(self, node: Node) -> None:
        prev_tail = self.tail
        self.tail = node
        prev_tail.next_node = node
        self.tail.prev_node = prev_tail
        self.tail.next_node = None
        self.tracker[node.key] = node        


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
