from typing import List

class Solution:
    def kthSmallestProduct(self, nums1: List[int], nums2: List[int], k: int) -> int:
        low = min(nums1[0]*nums2[0], nums1[0]*nums2[-1], nums1[-1]*nums2[0], nums1[-1]*nums2[-1])
        high = max(nums1[0]*nums2[0], nums1[0]*nums2[-1], nums1[-1]*nums2[0], nums1[-1]*nums2[-1])
        smallest = low

        nums1_negs = [el for el in nums1 if el < 0]
        nums1_zeroes = [el for el in nums1 if el == 0]
        nums1_poss = [el for el in nums1 if el > 0]
        nums2_negs = [el for el in nums2 if el < 0]
        nums2_zeroes = [el for el in nums2 if el == 0]
        nums2_poss = [el for el in nums2 if el > 0]

        def count_leq(x):
            count = 0
            
            if x < 0:
                nums2_negs_incrementor = -1
                for idx, el in enumerate(nums1_poss):
                    while nums2_negs_incrementor + 1 < len(nums2_negs):
                        if el * nums2_negs[nums2_negs_incrementor + 1] > x:
                            break
                        else:
                            nums2_negs_incrementor += 1
                    count += nums2_negs_incrementor + 1
                
                nums2_poss_incrementor = 0
                for idx, el in enumerate(nums1_negs):
                    while nums2_poss_incrementor < len(nums2_poss):
                        if el * nums2_poss[nums2_poss_incrementor] > x:
                            nums2_poss_incrementor += 1
                        else:
                            break
                    count += len(nums2_poss) - nums2_poss_incrementor
            elif x >= 0:
                # zeroes automatically make it
                count += (len(nums1_zeroes) * len(nums2)) + (len(nums2_zeroes) * len(nums1_negs)) + (len(nums2_zeroes) * len(nums1_poss))
                
                # negs automatically make it
                count += (len(nums1_poss) * len(nums2_negs)) + (len(nums1_negs) * len(nums2_poss))

                nums2_poss_incrementor = len(nums2_poss) - 1
                for idx, el in enumerate(nums1_poss):
                    while nums2_poss_incrementor > - 1:
                        if el * nums2_poss[nums2_poss_incrementor] > x:
                            nums2_poss_incrementor -= 1
                        else:
                            break
                    count += nums2_poss_incrementor + 1
                
                nums2_negs_incrementor = len(nums2_negs)
                for idx, el in enumerate(nums1_negs):
                    while nums2_negs_incrementor > 0:
                        if el * nums2_negs[nums2_negs_incrementor - 1] > x:
                            break
                        else:
                            nums2_negs_incrementor -= 1
                    count += len(nums2_negs) - nums2_negs_incrementor

            return count
        
        while low < high:
            mid = low + (high - low) // 2
            if count_leq(mid) >= k:
                high = mid
                smallest = high
            else:
                low = mid + 1
                smallest = low
        return smallest 

s = Solution()
print(s.kthSmallestProduct([-2,-1,0,1,2], [-3,-1,2,4,5], 3))