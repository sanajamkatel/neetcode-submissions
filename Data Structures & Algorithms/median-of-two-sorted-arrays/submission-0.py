class Solution:
    def findMedianSortedArrays(self, nums1: List[int], nums2: List[int]) -> float:
        final_nums = nums1 + nums2
        final_nums.sort()
        n= len(final_nums) 
        if n % 2 == 1:
            return final_nums[n // 2]

        else:
            middle1 = final_nums[n // 2 - 1]
            middle2 = final_nums[n // 2]
            return ( middle1 + middle2) /2