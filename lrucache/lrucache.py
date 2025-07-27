# TO DO
# for a single breach a single eviction maintains the correct head, tail and tracker
# 

"""
LRUCache lRUCache = new LRUCache(2);
lRUCache.put(1, 1); // cache is {1=1}
lRUCache.put(2, 2); // cache is {1=1, 2=2}
lRUCache.get(1);    // return 1
lRUCache.put(3, 3); // LRU key was 2, evicts key 2, cache is {1=1, 3=3}
lRUCache.get(2);    // returns -1 (not found)
lRUCache.put(4, 4); // LRU key was 1, evicts key 1, cache is {4=4, 3=3}
lRUCache.get(1);    // return -1 (not found)
lRUCache.get(3);    // return 3
lRUCache.get(4);    // return 4
"""

from typing import Any

class Node:
    def __init__(self, key: int, val: int):
        self.key = key
        self.val = val
        self.next_node: Node | None = None
        self.prev_node: Node | None = None

class LRUCache:

    def __init__(self, capacity: int, tracker: dict = {}):
        self.capacity = capacity
        self.tracker = tracker
        self.head: Node | None = None
        self.tail: Node | None = None

    def get(self, key: int) -> int:
        try:
            node = self.tracker[key]
            self.remove(key)
            self.add_to_tail(node)
            return node.val
        except KeyError:
            return -1

    def put(self, key: int, val: int) -> None:
        if self.head:
            if key in self.tracker:
                self.remove(key)
                self.add_to_tail(Node(key, val))
                return None
            elif len(self.tracker.keys()) == self.capacity:
                prev_head_key = self.head.key
                self.head = self.head.next_node
                self.remove(prev_head_key)
            self.add_to_tail(Node(key, val))
        else:
            self.tracker[key] = Node(key, val)
            self.head = self.tracker[key]
            self.tail = self.tracker[key]
        return None

    def remove(self, key: int) -> None:
        try:
            node = self.tracker[key]
            del self.tracker[key]
        except KeyError as e:
            return
        try:
            node.prev_node.next_node = node.next_node
        except AttributeError:
            pass
        try:    
            node.next_node.prev_node = node.prev_node
        except AttributeError:
            pass
    
    def add_to_tail(self, node: Node) -> None:
        prev_tail = self.tail
        self.tail = node
        self.tail.prev_node = prev_tail
        self.tail.prev_node.next_node = self.tail
        self.tracker[self.tail.key] = self.tail

# test LRUCache functionality
#lru = LRUCache(2)
#print(lru.head)
#print(lru.tail)
#print(lru.tracker)
#print(lru.capacity)
#del lru

# test single LRUCache.put functionality
#lru = LRUCache(2)
#lru.put(1,1)
#assert lru.tracker
#assert lru.tracker[1] is lru.head, "head is incorrect"
#assert lru.tracker[1] is lru.tail, "tail is incorrect"
#del lru


# test double LRUCache.put functionality
#lru = LRUCache(2)
#lru.put(1,1)
#lru.put(2,2)
#l = []
#for v in lru.tracker.values():
#    l.append(v)
#assert lru.tracker.get(1) is l[0], "LRUCache is disordered"
#assert lru.tracker.get(2) is l[1], "LRUCache is disordered"
#del lru, l

# test capacity breach maintains correct order
#lru = LRUCache(2)
#lru.put(1,1)
#lru.put(2,2)
#lru.put(3,3)
#l = []
#for v in lru.tracker.values():
#    l.append(v)
#assert 1 not in lru.tracker, "N1 remains in LRUCache"
#assert lru.tracker.get(2) is l[0], "LRUCache is disordered"
#assert lru.tracker.get(3) is l[1], "LRUCache is disordered"
#del lru, l

# test capacity breach maintains correct order
lru = LRUCache(2)
lru.put(1,1)
lru.put(2,2)
lru.put(3,3)
l = []
for v in lru.tracker.values():
    l.append(v)
assert lru.capacity == 2, "LRUCache capacity is not 2"
assert 1 not in lru.tracker, "N1 remains in LRUCache"
assert lru.tracker.get(2) is l[0], "LRUCache is disordered"
assert lru.tracker.get(3) is l[1], "LRUCache is disordered"
#del lru, l

# test double capacity breach maintains correct order
#lru = LRUCache(2)
#lru.put(1,1)
#lru.put(2,2)
#lru.put(3,3)
#lru.put(4,4)
#l = []
#for v in lru.tracker.values():
#    l.append(v)
#assert lru.capacity == 2, "LRUCache capacity is not 2"
#assert 1 not in lru.tracker, "N1 remains in LRUCache"
#assert lru.tracker.get(3) is l[0], "LRUCache is disordered"
#assert lru.tracker.get(4) is l[1], "LRUCache is disordered"
#del lru, l


# ["LRUCache","put","put","get","put","get","put","get","get","get"]
# [[2],[1,1],[2,2],[1],[3,3],[2],[4,4],[1],[3],[4]]

# expected
# [null,null,null,1,null,-1,null,-1,3,4]