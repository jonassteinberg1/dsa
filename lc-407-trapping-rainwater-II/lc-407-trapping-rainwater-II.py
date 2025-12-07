from typing import List

import heapq

class Solution:
    def trapRainWater(self, heightMap: List[List[int]]) -> int:

        # need at least 3 grid rows
        # to trap water
        if len(heightMap) < 3:
            return 0

        water = []

        for h in heightMap:
            for i, j in enumerate(h):
                # left: consider dropping lists that can't
                # be trap candidates for example the edge lists
                # and also drop the edge neighbors
                # up
                if i > 0:
                    h[i - 1] - h[i]
                # left
                if 

s = Solution()
s.trapRainWater([[1, 1, 1], [1, 0, 1], [1, 1, 1]])