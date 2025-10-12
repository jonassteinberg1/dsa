from typing import List

class Solution:
    def kthSmallestProduct(self, nums1: List[int], nums2: List[int], k: int) -> int:
        # l & r neg
        if nums1[0] < 0 and nums1[-1] < 0 and nums2[0] < 0 and nums2[-1] < 0:
            min_product = nums1[0] * nums2[0]
            max_product = nums1[-1] * nums2[-1]
            cursor1_start = -1
            cursor1_incrementor = -1
            cursor2_start = -1
            cursor2_incrementor = -1
        # l & r both pos
        elif nums1[0] >= 0 and nums1[-1] >= 0 and nums2[0] >= 0 and nums2[-1] >= 0:
            min_product = nums1[0] * nums2[0]
            max_product = nums1[-1] * nums2[-1]
            cursor1_start = 0
            cursor1_incrementor = 1
            cursor2_start = 0
            cursor2_incrementor = 1
        # l neg, r pos
        elif nums1[0] < 0 and nums1[-1] < 0 and nums2[0] >= 0 and nums2[-1] >= 0:
            min_product = nums1[0] * nums2[-1]
            max_product = nums1[-1] * nums2[0]
            cursor1_start = 0
            cursor1_incrementor = 1
            cursor2_start = -1
            cursor2_incrementor = -1
        # l pos, r neg
        elif nums1[0] >= 0 and nums1[-1] >= 0 and nums2[0] < 0 and nums2[-1] < 0:
            min_product = nums1[-1] * nums2[0]
            max_product = nums1[0] * nums2[-1]
            cursor1_start = -1
            cursor1_incrementor = -1
            cursor2_start = 0
            cursor2_incrementor = 1
        # l pos, r neg-to-pos
        # TODO
        elif nums1[0] >= 0 and nums1[-1] >= 0 and nums2[0] < 0 and nums2[-1] >= 0:
            min_product = nums1[-1] * nums2[0]
            max_product = nums1[-1] * nums2[-1]
            cursor1_start = -1
            cursor1_incrementor = -1
            cursor2_start = 0
            cursor2_incrementor = 1
        # l neg-to-pos, r pos
        # TODO
        elif nums1[0] < 0 and nums1[-1] >= 0 and nums2[0] >= 0 and nums2[-1] >= 0:
            min_product = nums1[0] * nums2[-1]
            max_product = nums1[-1] * nums2[-1]
            cursor1_start = 0
            cursor1_incrementor = 1
            cursor2_start = -1
            cursor2_incrementor = -1
        # l neg, r neg-to-pos
        elif nums1[0] < 0 and nums1[-1] < 0 and nums2[0] < 0 and nums2[-1] >= 0:
            min_product = nums1[0] * nums2[-1]
            max_product = nums1[0] * nums2[0]
            cursor1_start = -1
            cursor1_incrementor = -1
            cursor2_start = 0
            cursor2_incrementor = 1
        # l neg-to-pos, r neg
        elif nums1[0] < 0 and nums1[-1] >= 0 and nums2[0] < 0 and nums2[-1] < 0:
            min_product = nums1[-1] * nums2[0]
            max_product = nums1[0] * nums2[0]
            cursor1_start = -1
            cursor1_incrementor = -1
            cursor2_start = 0
            cursor2_incrementor = 1
        # l & r neg-to-pos
        elif nums1[0] < 0 and nums1[-1] >= 0 and nums2[0] < 0 and nums2[-1] >= 0:
            min_product = nums1[-1] * nums2[0]
            max_product = nums1[-1] * nums2[-1]
            cursor1_start = -1
            cursor1_incrementor = -1
            cursor2_start = -1
            cursor2_incrementor = -1
        low = min_product
        high = max_product
        counter = 0
        ks = []
        cursor1 = cursor1_start
        cursor2 = cursor2_start
        while low < high:
            mid = low + (high - low) // 2
            if nums1[cursor1] * nums2[cursor2] <= mid:
                counter += 1
                cursor2 += cursor2_incrementor
            elif cursor2 < len(nums2) - 1:
                cursor2 += cursor2_incrementor
            elif cursor1 < len(nums1) - 1:
                cursor1 += cursor1_incrementor
                cursor2 = cursor2_start
            else:
                if counter >= k:
                    high = mid - 1
                    counter = 0
                else:
                    low = mid + 1
                cursor1 = cursor1_start
                cursor2 = cursor2_start
        return mid

s = Solution()
print(s.kthSmallestProduct([4, 5, 6, 7], [100, 1000, 10000], 10))

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