from typing import List

class Solution:
    def kthSmallestProduct(self, nums1: List[int], nums2: List[int], k: int) -> int:
        # get the min max product range which means having to compute the signs of all array ends
        # binary search over this range
        # for each midpoint use two-pointers across nums1 and nums2 to count the number of product pairs smaller than the midpoint
        # find the smallest x that contains at least k-such pairs which
        if nums1[0] < 0 and nums2[0] < 0:
            if nums1[0] < nums2[0]:
                min = nums1[0] * nums2[-1]
                max = nums1[-1] * nums2[-1]
            else:
                min = nums1[-1] * nums2[0]
                max = nums1[-1] * nums2[-1]
        elif nums1[0] < 0 and nums2[0] >= 0:
            min = nums1[0] * nums2[-1]
            max = nums1[-1] * nums2[-1]
        elif nums1[0] >= 0 and nums2[0] < 0:
            min = nums1[-1] * nums2[0]
            max = nums1[-1] * nums[-1]
        else:
            min = nums1[0] * nums2[0]
            max = nums1[-1] * nums1[-1]
        
        low = min
        high = max
        cursor1 = 0
        cursor2 = 0
        counter = 0
        while low <= high:
            mid = low + (high - low) // 2
            if nums1[cursor1] * nums2[cursor2] <= mid and cursor2 < len(nums2):
                counter += 1
                cursor2 += 1
            elif nums1[cursor1] * nums2[cursor2] <= mid and cursor1 < len(nums1) - 1:
                    counter += 1
                    cursor1 += 1

s = Solution()
print(s.kthSmallestProduct([1, 2, 3, 4], [5, 6, 7, 8], 2))


