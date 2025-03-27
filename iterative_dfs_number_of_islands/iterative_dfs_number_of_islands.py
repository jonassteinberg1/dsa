from typing import List

class Solution:
    def numIslands(self, grid: List[List[str]]) -> int:
        
        islands = 0
        tracker = []
        
        for idx, l in enumerate(grid):
            for lidx, el in enumerate(l):
                if l[lidx] == '1':
                    tracker.append((idx, lidx))
                    islands += 1
                    while len(tracker) > 0:
                        start = tracker.pop()
                        grid[idx][lidx] = 0 # prevent double visit
                        if start[1] + 1 < len(grid[idx]):
                            if grid[start[0]][start[1]+1] == '1':
                                tracker.append((start[0], start[1]+1))
                                grid[start[0]][start[1]+1] = 0
                        if start[1] - 1 >= 0:
                            if grid[start[0]][start[1]-1] == '1':
                                tracker.append((start[0], start[1]-1))
                                grid[start[0]][start[1]-1] = 0
                        if start[0] + 1 < len(grid):
                            if grid[start[0]+1][start[1]] == '1':
                                tracker.append((start[0]+1, start[1]))
                                grid[start[0]+1][start[1]] = 0
                        if start[0] - 1 >= 0:
                            if grid[start[0]-1][start[1]] == '1':
                                tracker.append((start[0]-1, start[1]))
                                grid[start[0]-1][start[1]] = 0
        print(f"islands: {islands}")
        return islands

s = Solution()
s.numIslands(
[["1","1","0","0","0"],["1","1","0","0","0"],["0","0","1","0","0"],["0","0","0","1","1"]])