from typing import List

import heapq

class Solution:
    def trapRainWater(self, heightMap: List[List[int]]) -> int:

        # need at least 3 grid rows
        # to trap water
        if len(heightMap) < 3:
            return 0

        water = []
        neighbors = []

        for h in heightMap:
            for i, j in enumerate(h):
                # 1. a non-edge height differences imply trapability
                # 2. non-edge height differences are okay
                # look:
                #   if you're an edge -- no
                #   if you're not an edge -- maybe
                #     if neighbor_diff > 0
                #       trapability == least_neighbor_diff

s = Solution()
s.trapRainWater([[1, 1, 1], [1, 0, 1], [1, 1, 1]])