from random import randint

from typing import List, Tuple

class Solution:

    def __init__(self, w: List[int]):
        self.w = sorted(w)
        self.w_sum = sum(self.w)
        self.prefix_sums = []
        self.prefix_sums.append((1, self.w[0])) # need to handle for 1 in w
        self.prefix_sums.append((self.w[0] + 1, self.w[0] + self.w[1])) # need to handle for 1 in w
        for idx, val in enumerate(self.w, start=2):
            if idx < len(self.w):
                self.prefix_sums.append((self.prefix_sums[idx-1][1] + 1, sum(self.w[0:idx+1])))

    def pickIndex(self) -> int:
        t = randint(1, self.w_sum)
        low = 0
        high = len(self.prefix_sums) - 1
        while low <= high:
            middle = low + ((high - low) // 2) # this special configuration avoids the (high + low) // 2 configuration which as a corner case may exceed the max value a 32-bit integer can store
            if t == self.prefix_sums[middle][0] or t == self.prefix_sums[middle][1]:
                return middle
            elif t < self.prefix_sums[middle][0]:
                high = middle - 1
            elif t > self.prefix_sums[middle][1]:
                low = middle + 1
            else:
                # this linear search implies n + log(n)
                # hence a better design is needed
                for el in range(self.prefix_sums[middle][0], self.prefix_sums[middle][1]):
                    if t == el:
                        return middle

s = Solution([1, 517])
print(s.pickIndex())