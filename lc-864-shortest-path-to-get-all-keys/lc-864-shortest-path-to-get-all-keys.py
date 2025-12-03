from collections import deque
from typing import List

class Solution:
    def shortestPathAllKeys(self, grid: List[str]) -> int:

        locks = 0
        lock_moves = 0
        collected_keys = []

        for i, l in enumerate(grid):
            for j in l:
                if j in ['a', 'b', 'c', 'd', 'e', 'f', 'g']:
                    locks += 1

        class Found(Exception): pass

        try:
            for i, l in enumerate(grid):
                for j, m in enumerate(l):
                    if m == '@':
                        raise Found
        except Found:
            start = [i, j]

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
                    move.append([i-1, j])
                # index condition for looking down
                if i < len(grid) - 1 and [i+1, j] not in seen:
                    move.append([i+1, j])
                # index condition for looking left
                if j > 0 and [i, j-1] not in seen:
                    move.append([i, j-1])
                # index condition for looking right
                if j < len(l) - 1 and [i, j+1] not in seen:
                    move.append([i, j+1])
        
                return move

        class NoMoreLocks(Exception): pass

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
                    lock_moves += 1
                elif grid[move[0]][move[1]] in ['a', 'b', 'c', 'd', 'e', 'f']:
                    d.append(move)
                    lock_moves += 1
                    locks -= 1
                    collected_keys.append(grid[move[0]][move[1]])
                    try:
                        if locks == 0:
                            raise NoMoreLocks
                    except NoMoreLocks:
                        return lock_moves
                else:
                    if grid[move[0]][move[1]].lower() in collected_keys:
                        d.append(move)

        return lock_moves

s = Solution()
s.shortestPathAllKeys(["@..aA","..B#.","....b"])

