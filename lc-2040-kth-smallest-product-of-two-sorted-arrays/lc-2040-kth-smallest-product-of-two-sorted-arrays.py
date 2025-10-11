from typing import List

class Solution:
    def kthSmallestProduct(self, nums1: List[int], nums2: List[int], k: int) -> int:
        # l & r neg
        if nums1[0] < 0 and nums1[-1] < 0 and nums2[0] < 0 and nums2[-1] < 0:
            min_product = nums1[0] * nums2[0]
            max_product = nums1[-1] * nums2[-1]
            cursor1 = -1
            cursor1_incrementor = -1
            cursor2 = -1
            cursor2_incrementor = -1
        # l & r both pos
        elif nums1[0] >= 0 and nums1[-1] >= 0 and nums2[0] >= 0 and nums2[-1] >= 0:
            min_product = nums1[0] * nums2[0]
            max_product = nums1[-1] * nums2[-1]
            cursor1 = 0
            cursor1_incrementor = 1
            cursor2 = 0
            cursor2_incrementor = 1
        # l neg, r pos
        elif nums1[0] < 0 and nums1[-1] < 0 and nums2[0] >= 0 and nums2[-1] >= 0:
            min_product = nums1[0] * nums2[-1]
            max_product = nums1[-1] * nums2[0]
            cursor1 = 0
            cursor1_incrementor = 1
            cursor2 = -1
            cursor2_incrementor = -1
        # l pos, r neg
        elif nums1[0] >= 0 and nums1[-1] >= 0 and nums2[0] < 0 and nums2[-1] < 0:
            min_product = nums1[-1] * nums2[0]
            max_product = nums1[0] * nums2[-1]
            cursor1 = -1
            cursor1_incrementor = -1
            cursor2 = 0
            cursor2_incrementor = 1
        # l pos, r neg-to-pos
        # TODO
        elif nums1[0] >= 0 and nums1[-1] >= 0 and nums2[0] < 0 and nums2[-1] >= 0:
            min_product = nums1[-1] * nums2[0]
            max_product = nums1[-1] * nums2[-1]
            cursor1 = -1
            cursor1_incrementor = -1
            cursor2 = 0
            cursor2_incrementor = 1
        # l neg-to-pos, r pos
        # TODO
        elif nums1[0] < 0 and nums1[-1] >= 0 and nums2[0] >= 0 and nums2[-1] >= 0:
            min_product = nums1[0] * nums2[-1]
            max_product = nums1[-1] * nums2[-1]
            cursor1 = 0
            cursor1_incrementor = 1
            cursor2 = -1
            cursor2_incrementor = -1
        # l neg, r neg-to-pos
        elif nums1[0] < 0 and nums1[-1] < 0 and nums2[0] < 0 and nums2[-1] >= 0:
            min_product = nums1[0] * nums2[-1]
            max_product = nums1[0] * nums2[0]
            cursor1 = -1
            cursor1_incrementor = -1
            cursor2 = 0
            cursor2_incrementor = 1
        # l neg-to-pos, r neg
        elif nums1[0] < 0 and nums1[-1] >= 0 and nums2[0] < 0 and nums2[-1] < 0:
            min_product = nums1[-1] * nums2[0]
            max_product = nums1[0] * nums2[0]
            cursor1 = -1
            cursor1_incrementor = -1
            cursor2 = 0
            cursor2_incrementor = 1
        # l & r neg-to-pos
        elif nums1[0] < 0 and nums1[-1] >= 0 and nums2[0] < 0 and nums2[-1] >= 0:
            min_product = nums1[-1] * nums2[0]
            max_product = nums1[-1] * nums2[-1]
            cursor1 = -1
            cursor1_incrementor = -1
            cursor2 = -1
            cursor2_incrementor = -1
        low = min_product
        high = max_product
        counter = 0
        ks = []
        while low < high:
            mid = low + (high - low) // 2
            if nums1[cursor1] * nums2[cursor2] <= mid:
                counter += 1
                if cursor2 < len(nums2) - 1:
                    cursor2 += cursor2_incrementor
                elif cursor1 < len(nums1) - 1:
                    cursor1 += cursor1_incrementor
                    cursor2 = cursor2_incrementor
            else:
                if counter >= k:
                    ks.append(mid)
                high = mid - 1
                counter = 0
                cursor1 = cursor1_incrementor
                cursor2 = cursor2_incrementor
        return min(ks)

s = Solution()
print(s.kthSmallestProduct([-1, 1, 2, 3, 4], [-8, -7, -6, -5], 3))

# r & l neg
[-2 -1], [-3, -2]

# r & l neg-to-pos
[-1, 0], [-1, 0]

# l neg, r neg-to-pos
[-2 -1], [-1, 3]

# l neg-to-pos, r neg
[-1, 1], [-2, -1]

# l pos, r neg-to-pos
[0, 1], [-1, 0]

# l neg, r pos
[-2, -1], [1, 2]

# l pos, r neg
[1, 2], [-2, -1]

# r & l pos
[0, 1], [0, 1]