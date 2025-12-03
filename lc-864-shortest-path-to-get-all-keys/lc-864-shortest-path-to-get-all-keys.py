from collections import deque
from typing import List

class Solution:
    def shortestPathAllKeys(self, grid: List[str]) -> int:

        class Found(Exception):
            pass

        try:
            for i, l in enumerate(grid):
                for j, m in enumerate(l):
                    if m == '@':
                        raise Found
        except Found:
            start = [i, j, set()]

        d = deque()
        d.append(start)
        seen = []
        seen.append(start)

        def look(node: List[int]) -> List[str]:
                i = node[0]
                j = node[1]
                move = []
                # index condition for looking up
                if i > 0 and [i-1, j] not in seen:
                    move.append([i-1, j], set())
                # index condition for looking down
                if i < len(grid) - 1 and [i+1, j] not in seen:
                    move.append([i+1, j], set())
                # index condition for looking left
                if j > 0 and [i, j-1] not in seen:
                    move.append([i, j-1], set())
                # index condition for looking right
                if j < len(l) - 1 and [i, j+1] not in seen:
                    move.append([i, j+1], set())
        
                return move

        while d:
            # remember -- this is fifo so we must popleft()
            current = d.popleft() # need to mark visited next
            moves = look(current)
            for move in moves:
                seen.append(move)
                if grid[move[0]][move[1]] == '#':
                    pass
                elif grid[move[0]][move[1]] == '.':
                    d.append(move)
                elif grid[move[0]][move[1]] in ['a', 'b', 'c', 'd', 'e', 'f']:
                    move[2].add(grid[move[0]][move[1]])
                    d.append(move)
                else:
                    if grid[move[0]][move[1]].lower() in move[2]:
                        d.append(move)

        return 

s = Solution()
s.shortestPathAllKeys(["@..aA","..B#.","....b"])

