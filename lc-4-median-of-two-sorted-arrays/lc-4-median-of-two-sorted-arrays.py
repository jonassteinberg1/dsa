class Solution:
    def findMedianSortedArrays(self, nums1: List[int], nums2: List[int]) -> float:
        pass
        # sorted arrays --> binary search
        # searching arrays to find a median --> binary search
        # the question isn't asking for mutation in anyway but traversal --> search --> sorted arrays --> binary search

        # approach
        # 
        # question is not asking for mutation, it's asking for a result
        # the result is a value
        # the value is a median from two sorted arrays
        # search
        # binary search
        # median: if len(m) !% 2 then get middle element
        # median: if len(n) % 2 then sum two middle elements and divide by two and return result
        # in the case of two sorted arrays though you can
        # get the median of both and then take the median again
        # but there is probably some trick
        #
        # the question specifies to merge the arrays
        # m <= 1000, n <= 1000 and m + n <= 2000
        # -10^6 <= values <= 10^6
        #
        # [1, 2, 3], [5, 6, 9] --> [1, 2, 3, 5, 6, 9] --> (3+5)/2 = 4
        # [6, 9, 20], [4, 17, 69] --> [6, 9, 20, 4, 17, 69] --> sort
        # here's what needs to be solved:
        # both arrays are sorted but the merged array is not
        # so how can you produce a merged array in O(log(m+n))?