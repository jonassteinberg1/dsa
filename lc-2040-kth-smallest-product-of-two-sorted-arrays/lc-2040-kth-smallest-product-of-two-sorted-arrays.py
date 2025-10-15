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
                    while len(nums2_negs) - nums2_negs_incrementor > 0:
                        if el * nums2_negs[nums2_negs_incrementor] > x:
                            incrementor += 1
                            if incrementor == len(nums2):
                                incrementor = 0
                                break
                        else:
                            count += len(nums2) - incrementor
                            break
            
            # TO DO
            # 1. build out  if el * nums2_negs[nums2_negs_incrementor] <= x for nums1_poss x nums2_negs
            # 2. repeat for other relevant segments
            # 3. build out x > 0 NOTE: x == 0 already handled above


            


        def count_leq(x):
            count = 0
            incrementor = 0
            for idx, el in enumerate(nums1):
                if el > 0:
                    while len(nums2) - incrementor > 0:
                        if el * nums2[len(nums2) - incrementor - 1] > x:
                            incrementor += 1
                            if incrementor == len(nums2):
                                incrementor = 0
                                break
                        else:
                            count += len(nums2) - incrementor
                            if (idx < len(nums1) - 1) and ((nums1[idx] < 0 and nums1[idx + 1] >= 0) or (nums1[idx] >= 0 and nums1[idx+1] < 0) or (nums1[0] < 0 and nums1[-1] <0) or (nums2[0] < 0 and nums2[-1] <0)):
                                incrementor = 0
                            break
                else:
                    while incrementor < len(nums2):
                        if el * nums2[incrementor] > x:
                            incrementor += 1
                            if incrementor == len(nums2):
                                incrementor = 0
                                break
                        else:
                            count += len(nums2) - incrementor
                            if (idx < len(nums1) - 1) and ((nums1[idx] < 0 and nums1[idx + 1] >= 0) or (nums1[idx] >= 0 and nums1[idx+1] < 0) or (nums1[0] < 0 and nums1[-1] <0) or (nums2[0] < 0 and nums2[-1] <0)):
                                incrementor = 0
                            break
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
print(s.kthSmallestProduct([-3,-1,5,6], [-10,-7,-6,-5,-5,-4,-1,7,8], 28))