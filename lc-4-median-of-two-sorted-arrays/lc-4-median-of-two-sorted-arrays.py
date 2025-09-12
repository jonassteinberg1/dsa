from typing import List

class Solution:
    @classmethod
    def findMedianSortedArrays(self, nums1: List[int], nums2: List[int]) -> float:
        self.nums1 = nums1
        self.nums2 = nums2

        if self.nums1[0] >= self.nums2[-1]:
            if len(self.nums1 + self.nums2) % 2 == 0:
                middle = len(self.nums2 + self.nums1) // 2
                return sum((self.nums2 + self.nums1)[middle-1:middle+1]) / 2
            else:
                return (self.nums2 + self.nums1)[len(self.nums2 + self.nums1) // 2]
        elif self.nums1[-1] <= self.nums2[0]:
            if len(self.nums1 + self.nums2) % 2 == 0:
                middle = len(self.nums1 + self.nums2) // 2
                return sum((self.nums1 + self.nums2)[middle-1:middle+1]) / 2
            else:
                return (self.nums1 + self.nums2)[len(self.nums1 + self.nums2) // 2]

print(Solution.findMedianSortedArrays([1, 2, 3], [4, 5, 6]))