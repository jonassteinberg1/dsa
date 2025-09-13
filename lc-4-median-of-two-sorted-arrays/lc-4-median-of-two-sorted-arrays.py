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
        elif len(self.nums1) < 2:
            lo = 0
            hi = self.nums2[-1]
            while lo <= hi:
                middle = lo + (high - lo) // 2
                if self.nums1[0] == middle:
                    if len(self.nums1 + self.nums2) % 2 == 0:
                        middle = len(self.nums1 + self.nums2) // 2
                        return sum(sorted(self.nums1 + self.nums2)[middle-1:middle+1]) / 2
                    else:
                        return (sorted(self.nums1 + self.nums2))[len(self.nums1 + self.nums2) // 2]
                elif self.nums1 > middle:
                    lo = middle + 1
                else:
                    high = middle - 1
        elif len(self.nums2) < 2:
            lo = 0
            hi = self.nums1[-1]
            while lo <= hi:
                middle = lo + (high - lo) // 2
                if self.nums2[0] == middle:
                    if len(self.nums1 + self.nums2) % 2 == 0:
                        middle = len(self.nums1 + self.nums2) // 2
                        return sum(sorted(self.nums1 + self.nums2)[middle-1:middle+1]) / 2
                    else:
                        return (sorted(self.nums1 + self.nums2))[len(self.nums1 + self.nums2) // 2]
                elif self.nums2 > middle:
                    lo = middle + 1
                else:
                    high = middle - 1
    
            
        else:
            if len(self.nums1) <= len(self.nums2):
                short = self.nums1
                long = self.nums2
            else:
                short = self.nums2
                long = self.nums1
            half = (len(short) + len(long) + 1) // 2
            lo = max(0, half - len(long))
            hi = min(len(short), half)
            while lo <= hi:
                i = lo + (hi - lo) // 2
                j = half - i
                if short[i-1] <= long[j] and long[j-1] <= short[i]:
                    if len(short + long) % 2 != 0:
                        return max(short[i-1], long[j-1])
                    else:
                        return (max(short[i-1], long[j-1]) + min(short[i], long[j]))/2
                elif short[i-1] > long[j]:
                    hi = i - 1
                else:
                    lo = i + 1

            
        

           


print(Solution.findMedianSortedArrays([1, 3, 5, 900], [2]))