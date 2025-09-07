from random import choice

from typing import List

class Solution:

    def __init__(self, w: List[int]):
        self.w = w
        self.probs = []
        for idx, el in enumerate(self.w):
            for r in range(0, el):
                self.probs.append(idx)

    def pickIndex(self) -> int:
        return choice(self.probs)

s = Solution([1, 2, 3, 4 ,5])
print(s.pickIndex())


