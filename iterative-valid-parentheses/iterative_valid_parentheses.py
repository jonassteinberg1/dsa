from queue import deque

class Solution:
    def isValid(self, s: str) -> bool:
        pairs = {')': '(', ']': '[', '}': '{'}
        stack = deque()
        for el in s:
            if el in pairs.values():
                stack.append(el)
            elif el in pairs.keys():
                if len(stack) == 0:
                    return False
                elif pairs[el] == stack[-1]:
                    stack.pop()
                else:
                    return False
        return len(stack) == 0

