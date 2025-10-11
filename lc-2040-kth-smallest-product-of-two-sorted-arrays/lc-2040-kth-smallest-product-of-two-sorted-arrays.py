from typing import List

class Solution:
    def kthSmallestProduct(self, nums1: List[int], nums2: List[int], k: int) -> int:
        # get the min max product range which means having to compute the signs of all array ends
        # binary search over this range
        # for each midpoint use two-pointers across nums1 and nums2 to count the number of product pairs smaller than the midpoint
        # find the smallest x that contains at least k-such pairs which
        if nums1[0] < 0 and nums2[0] < 0:
            if nums1[0] < nums2[0]:
                minn = nums1[0] * nums2[-1]
                max = nums1[-1] * nums2[-1]
            else:
                minn = nums1[-1] * nums2[0]
                max = nums1[0] * nums2[0]
        elif nums1[0] < 0 and nums2[0] >= 0:
            minn = nums1[0] * nums2[-1]
            max = nums1[-1] * nums2[-1]
        elif nums1[0] >= 0 and nums2[0] < 0:
            minn = nums1[-1] * nums2[0]
            max = nums1[-1] * nums[-1]
        else:
            minn = nums1[0] * nums2[0]
            max = nums1[-1] * nums1[-1]
        
        low = minn
        high = max
        cursor1 = 0
        cursor2 = 0
        counter = 0
        ks = []
        while low < high:
            mid = low + (high - low) // 2
            if nums1[cursor1] * nums2[cursor2] <= mid:
                counter += 1
                if cursor2 < len(nums2) - 1:
                    cursor2 += 1
                elif cursor1 < len(nums1) - 1:
                    cursor1 += 1
                    cursor2 = 0
            else:
                if counter >= k:
                    ks.append(mid)
                high = mid - 1
                counter = 0
                cursor1 = 0
                cursor2 = 0
        return min(ks)

s = Solution()
print(s.kthSmallestProduct([-1, 1, 2, 3, 4], [-8, -7, -6, -5], 3))



