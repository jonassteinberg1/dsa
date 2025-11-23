from collections import defaultdict, deque
from typing import List

class Solution:
    def collectTheCoins(self, coins: List[int], edges: List[List[int]]) -> int:
        if sum(coins) == 0:
            return 0
        
        adj = defaultdict(list)
        # edges compacts u, v and v, u into [u, v]
        for u, v in edges:
            adj[u].append(v)
            adj[v].append(u)
        
        # build degree list from adjacency list
        degrees = {u: len(v) for u, v in adj.items()}

        d = deque()

        # enqueue with coinless leaves first
        for u in adj.keys():
            if degrees[u] == 1 and coins[u] == 0:
                d.append(u)
        
        # BFS prune 1: coinless leaves
        while d:
            u = d.popleft()
            # no longer in the graph; deleting would be cleaner
            if degrees[u] > 0:
                degrees[u] = 0
                # can also skip "v" and just use the expression
                # adj[u][0] everywhere but u and v are "node" and "neighbor"
                # conventions
                for v in adj[u]:
                    if degrees[v] > 0:
                        degrees[v] -= 1
                        if degrees[v] == 1 and coins[v] == 0:
                            d.append(v)
        
        for u in adj.keys():
            if degrees[u] == 1:
                # d[u][1] is depth and tracking depth
                # is required for endpoint discount
                d.append((u, 0))
        
        # endpoint discount
        while d:
            u = d.popleft()
            if degrees[u[0]] > 0:
                depth = u[1]
                if depth < 2:
                    degrees[u[0]] = 0
                    for v in adj[u[0]]:
                        if degrees[v] > 0:
                            degrees[v] -= 1
                            if degrees[v] == 1:
                                d.append((v, depth + 1))
        
        # the values of degrees are ints so since
        # dict.values() returns a list it is in this
        # case a list of ints which is the natural
        # input for sum
        remaining_edges = sum(degrees.values())//2

        if remaining_edges == 0:
            return 0
        return 2 * remaining_edges
            


                




        

s = Solution()
s.collectTheCoins([1,0,0,0,0,1], [[0,1],[1,2],[2,3],[3,4],[4,5]])