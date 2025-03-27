import heapq

from typing import List

class Solution:
    def findKthLargest(self, nums: List[int], k: int) -> int:
        h = list()
        for num in nums:
            if len(h) < k:
                heapq.heappush(h, num)
            elif num > h[0]:
                heapq.heappop(h)
                heapq.heappush(h, num)
        root = heapq.heappop(h)
        return root

s = Solution()
s.findKthLargest([1, 2, 3], 2)