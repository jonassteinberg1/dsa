from random import choice

from typing import List

class Solution:

    def __init__(self, w: List[int]):
        self.w = w
        s = sum(self.w)
        self.prefix_sums = []
        self.prefix_sums.append((1, self.w[0]))
        self.prefix_sums.append((self.w[0] + 1, self.w[0] + self.w[1]))
        for idx, val in enumerate(self.w[2:]):
        #for idx, val in enumerate(self.w):
            if idx < len(self.w) - 1:
                self.prefix_sums.append((val + 1, (val + 1) + self.w[idx+1]))

    def pickIndex(self) -> int:
        #return choice(self.probs)
        return self.prefix_sums

s = Solution([1, 2, 3, 4 ,5])
print(s.pickIndex())