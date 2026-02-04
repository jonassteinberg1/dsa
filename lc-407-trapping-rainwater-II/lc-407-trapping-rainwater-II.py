from typing import List

import heapq

class Solution:
    def trapRainWater(self, heightMap: List[List[int]]) -> int:

        # need at least 3 grid rows
        # to trap water
        if len(heightMap) < 3:
            return 0

        water = []
        neighbors = [(1, 1)]
        visited = []

        # left off: if you have a difference in all four directions
        # the min of that difference is the water (?)
        # you could say if len(height_differences) == 4 then max?
        

        def look(start: List[int, int]):
            height_differences = []
            up = (start[0], start[1] - 1)
            up_height_difference = heightMap[start[0]][start[1]] - heightMap[up[0]][up[1]]
            if up_height_difference < 0 and up not in visited:
                heapq.heappush(height_differences, up_height_difference)
            if up[0] != 0 and up[0] != len(heightMap) - 1 and up[1] != 0 and up[1] != len(heightMap[up[0]]) - 1 and up not in visited and up not in neighbors:
                neighbors.append(up)
            left = (start[0] + 1, start[1])
            left_height_difference = heightMap[start[0]][start[1]] - heightMap[left[0]][left[1]]
            if left_height_difference < 0 and left not in visited:
                heapq.heappush(height_differences, left_height_difference)
            if left[0] != 0 and left[0] != len(heightMap) - 1 and left[1] != 0 and left[1] != len(heightMap[up[0]]) - 1 and left not in visited and left not in neighbors:
                neighbors.append(left)
            down = (start[0], start[1] + 1)
            down_height_difference = heightMap[start[0]][start[1]] - heightMap[down[0]][down[1]]
            if down_height_difference < 0 and down not in visited:
                heapq.heappush(height_differences, down_height_difference)
            if down[0] != 0 and down[0] != len(heightMap) - 1 and down[1] != 0 and down[1] != len(heightMap[up[0]]) - 1 and down not in visited and down not in neighbors:
                neighbors.append(down)
            right = (start[0] - 1, start[1])
            right_height_difference = heightMap[start[0]][start[1]] - heightMap[right[0]][right[1]]
            if right_height_difference < 0 and right not in visited:
                heapq.heappush(height_differences, right_height_difference)
            if right[0] != 0 and right[0] != len(heightMap) - 1 and right[1] != 0 and right[1] != len(heightMap[up[0]]) - 1 and right not in visited and right not in neighbors:
                neighbors.append(right)
            
            return height_differences
        
        while neighbors:
            current = heapq.heappop(neighbors)
            visited.append(current)
            height_differences = look(current)
            if height_differences:
                water.append(height_differences.pop())
        
        return -1 * sum(water)


s = Solution()
s.trapRainWater([[3,3,3,],[3,2,3],[3,1,3],[3,2,3],[3,3,3]])