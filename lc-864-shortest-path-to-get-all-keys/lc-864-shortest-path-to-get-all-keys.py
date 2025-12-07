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
            start = [i, j, set(), 0]
        
        keys = set()

        for i, l in enumerate(grid):
            for j in l:
                if j in ['a', 'b', 'c', 'd', 'e', 'f', 'g']:
                    keys.add(j)

        d = deque()
        d.append(start)
        seen = dict()
        seen[tuple(start[0:2])] = [start[2]]

        def look(node: List[int]) -> List[str]:
                i = node[0]
                j = node[1]
                move = []
                # index condition for looking up
                if i > 0:
                    move.append([i-1, j])
                # index condition for looking down
                if i < len(grid) - 1:
                    move.append([i+1, j])
                # index condition for looking left
                if j > 0:
                    move.append([i, j-1])
                # index condition for looking right
                if j < len(grid[i]) - 1:
                    move.append([i, j+1])
        
                return move

        while d:
            # remember -- this is fifo so we must popleft()
            current = d.popleft() # need to mark visited next
            moves = look(current)
            for move in moves:
                temp = set()
                temp = current[2].copy()
                if grid[move[0]][move[1]] == '#':
                    pass
                elif grid[move[0]][move[1]] == '.' or grid[move[0]][move[1]] == '@':
                    move.append(temp)
                    try:
                        seen[tuple(move[0:2])]
                        if temp not in seen[tuple(move[0:2])]:
                            seen[tuple(move[0:2])].append(temp)
                            move.append(current[3] + 1)
                            d.append(move)
                    except KeyError:
                        seen[tuple(move[0:2])] = [temp]
                        move.append(current[3] + 1)
                        d.append(move)
                elif grid[move[0]][move[1]] in keys:
                    temp.add(grid[move[0]][move[1]])
                    move.append(temp)
                    if move[2] == keys:
                        move.append(current[3] + 1)
                        print(move[3])
                        return move[3]
                    try:
                        seen[tuple(move[0:2])]
                        if temp not in seen[tuple(move[0:2])]:
                            seen[tuple(move[0:2])].append(temp)
                            move.append(current[3] + 1)
                            d.append(move)
                    except KeyError:
                        seen[tuple(move[0:2])] = [temp]
                        move.append(current[3] + 1)
                        d.append(move)
                else:
                    if grid[move[0]][move[1]].lower() in temp:
                        move.append(temp)
                        try:
                            seen[tuple(move[0:2])]
                            if temp not in seen[tuple(move[0:2])]:
                                seen[tuple(move[0:2])].append(temp)
                                move.append(current[3] + 1)
                                d.append(move)
                        except KeyError:
                            seen[tuple(move[0:2])] = [temp]
                            move.append(current[3] + 1)
                            d.append(move)
        
        return -1

s = Solution()
s.shortestPathAllKeys(["@...a",".###A","b.BCc"])

