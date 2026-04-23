class Solution:
    def findMedianSortedArrays(self, nums1: List[int], nums2: List[int]) -> float:
        i, j = 0, 0 
        median1 = median2 = 0

        total_len = len(nums1) + len(nums2)
        med = 0
        for count in range((total_len//2)+1):
            median2 = median1
            if i<len(nums1) and j < len(nums2):
                if nums1[i] < nums2[j]:
                    median1 = nums1[i]
                    i += 1
                else:
                    median1 = nums2[j]
                    j += 1
            elif i < len(nums1):
                median1 = nums1[i]
                i += 1
            else:
                median1 = nums2[j]
                j +=1
        
        if total_len % 2 == 1:
            return float(median1)
        else:
            return (median1+median2)/2.0