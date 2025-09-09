from random import choice

from typing import List

class Solution:

    def __init__(self, w: List[int]):
        self.w = w
        s = sum(self.w)
        self.prefix_sums = []
        self.prefix_sums.append((1, self.w[0])) # need to handle for 1 in w
        self.prefix_sums.append((self.w[0] + 1, self.w[0] + self.w[1])) # need to handle for 1 in w
        for idx, val in enumerate(self.w, start=2):
            #if idx < len(self.w):
            self.prefix_sums.append((self.prefix_sums[idx-1][1] + 1, sum(self.w[0:idx+1])))


    def pickIndex(self) -> int:
        return choice(self.w)

s = Solution([1, 2, 3, 4 ,5])
print(s.pickIndex())