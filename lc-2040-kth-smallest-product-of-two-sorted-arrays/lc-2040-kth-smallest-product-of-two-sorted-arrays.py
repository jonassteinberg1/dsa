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
            
            if nums1_zeroes and x >= 0:
                count += len(nums1_zeroes) * len(nums2)
            elif nums2_zeroes and x >= 0:
                count += len(nums1_zeroes) * len(nums2_zeroes)
            
            if x < 0:
                nums2_negs_incrementor = 0
                for idx, el in enumerate(nums1_poss):
                    while nums2_negs_incrementor < len(nums2_negs):
                        if el * nums2_negs[len(nums2_negs)- nums2_negs_incrementor - 1] > x:
                            nums2_negs_incrementor += 1
                            if nums2_negs_incrementor == len(nums2_negs):
                                nums2_negs_incrementor = 0
                                break
                        else:
                            count += len(nums2_negs) - nums2_negs_incrementor
                            nums2_negs_incrementor = 0
                            break
                
                nums2_poss_incrementor = 0
                for idx, el in enumerate(nums1_negs):
                    while nums2_poss_incrementor < len(nums2_poss):
                        if el * nums2_poss[len(nums2_poss) - nums2_poss_incrementor - 1] > x:
                            nums2_poss_incrementor += 1
                            if nums2_poss_incrementor == len(nums2_poss):
                                nums2_poss_incrementor = 0
                                break
                        else:
                            count += len(nums2_negs) - nums2_poss_incrementor
                            break
            elif x > 0:
                nums2_negs_incrementor = 0
                for idx, el in enumerate(nums1_poss):
                    while nums2_negs_incrementor < len(nums2_negs):
                        if el * nums2_negs[nums2_negs_incrementor] > x:
                            nums2_negs_incrementor += 1
                            if nums2_negs_incrementor == len(nums2_negs):
                                nums2_negs_incrementor = 0
                                break
                        else:
                            count += len(nums2_negs) - nums2_negs_incrementor
                            break
                
                nums2_poss_incrementor = 0
                for idx, el in enumerate(nums1_negs):
                    while nums2_poss_incrementor < len(nums2_poss):
                        if el * nums2_poss[len(nums2_poss) - nums2_poss_incrementor - 1] > x:
                            nums2_poss_incrementor += 1
                            if nums2_poss_incrementor == len(nums2_poss):
                                nums2_poss_incrementor = 0
                                break
                        else:
                            count += len(nums2_negs) - nums2_poss_incrementor
                            break
            return count
    
            # TO DO
            # 1. build out  if el * nums2_negs[nums2_negs_incrementor] <= x for nums1_poss x nums2_negs
            # 2. repeat for other relevant segments
            # 3. build out x > 0 NOTE: x == 0 already handled above
        
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
print(s.kthSmallestProduct([-3,-1,5,6], [-10,-7,-6,-5,-5,-4,-1,7,8], 28))