from random import choice

from typing import List, Tuple

class Solution:

    def __init__(self, w: List[int]):
        self.w = sorted(w)
        self.prefix_sums = []
        self.prefix_sums.append((1, self.w[0])) # need to handle for 1 in w
        self.prefix_sums.append((self.w[0] + 1, self.w[0] + self.w[1])) # need to handle for 1 in w
        for idx, val in enumerate(self.w, start=2):
            # don't think this if is ever needed
            # but not sure why
            #if idx < len(self.w):
            self.prefix_sums.append((self.prefix_sums[idx-1][1] + 1, sum(self.w[0:idx+1])))

    # TO DO:
    # still need a mapping structure
    # back to the weight indexes
    def binary_search(self, l: List[Tuple[int]], t: int):
        while low <= high:
            low = 0
            high = len(l) - 1
            middle = low + ((high - low) // 2) # this special configuration avoids the (high + low) // 2 configuration which as a corner case may exceed the max value a 32-bit integer can store
            if t == l[middle][0] or t == l[middle][1]:
                return t # this should return the weight index instead
            elif t < l[middle][0]:
                high = middle - 1
            elif t > l[middle][1]:
                low = middle + 1
            else:
                # this linear search implies n + log(n)
                # hence a better design is needed
                for el in range(l[middle][0], l[middle][1]):
                    if t == el:
                        return el 

        


    def pickIndex(self) -> int:
        return choice(self.w)

s = Solution([1, 2, 3, 4 ,5])
print(s.pickIndex())