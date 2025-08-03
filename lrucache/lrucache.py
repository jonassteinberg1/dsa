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
                self.add_to_tail(node)
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
                self.add_to_tail(node)
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
            if len(self.tracker.keys()) == 1 and self.capacity == 1:
                self.remove(key)
                self.tracker[key] = Node(key, val)
                self.head = self.tracker[key]
                self.tail = self.tracker[key]
            elif len(self.tracker.keys()) == 1:
                self.add(Node(key, int))
                self.head = self.tail.prev_node
            if key in self.tracker and len(self.tracker.keys()) == 1:
                self.remove(key)
                self.add_to_tail(Node(key, val))
            elif key in self.tracker:
                node = self.tracker[key]
                if key == self.head.key:
                    node.next_node.prev_node = None # make next node's (head) prev_node None
                    self.head = node.next_node
                    self.remove(key)
                    self.add_to_tail(Node(key, val))
                elif key == self.tail.key:
                    self.remove(key)
                    self.tail = Node(key, val)
                    node.prev_node.next_node = self.tail
                    self.tail.prev_node = node.prev_node
                    self.tail.next_node = None
                    self.tracker[self.tail.key] = self.tail  
                else:
                    node.prev_node.next_node = node.next_node
                    node.next_node.prev_node = node.prev_node
                    self.remove(key)
                    self.add_to_tail(Node(key, val))
                self.check(self.tracker, self.head, self.tail)
                return ['null']
            elif len(self.tracker.keys()) == self.capacity: # we shift left when we're at capacity
                prev_head_key = self.head.key # we just save this for the delete
                node = self.tracker.get(prev_head_key)
                if not node.prev_node and not node.next_node:
                    self.remove(prev_head_key)
                    self.tracker[key] = Node(key, val)
                    self.head = self.tracker[key]
                    self.tail = self.tracker[key]
                else:
                    self.head = self.head.next_node # current head's next node becomes head; preparing to shift left
                    self.head.prev_node = None # new head's prev_node None
                    self.remove(prev_head_key) # evict old head bc we're shifting left
                    self.add_to_tail(Node(key, val))
                    self.check(self.tracker, self.head, self.tail)
            else:
                self.add_to_tail(Node(key, val))
        else:
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

run([[2],[2,1],[2,2],[2],[1,1],[4,1],[2]])
