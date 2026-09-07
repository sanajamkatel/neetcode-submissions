class Solution:
    def findMedianSortedArrays(self, nums1: List[int], nums2: List[int]) -> float:
        # final_nums = nums1 + nums2
        # final_nums.sort()
        # n= len(final_nums) 
        # if n % 2 == 1:
        #     return final_nums[n // 2]

        # else:
        #     middle1 = final_nums[n // 2 - 1]
        #     middle2 = final_nums[n // 2]
        #     return ( middle1 + middle2) /2
        A, B = nums1, nums2
        total= len(A) + len(B)
        half= (total)//2
        if len(B) < len(A):
            A, B = B, A
        
        low = 0
        high = len(A) - 1
        while True:
            mid_for_A = (low + high ) // 2
            mid_for_B = half - mid_for_A - 2

            Aleft = A[mid_for_A] if mid_for_A >= 0 else float("-infinity")
            Aright = A[mid_for_A + 1] if (mid_for_A + 1) < len(A) else float("infinity")
            Bleft = B[mid_for_B] if mid_for_B >= 0 else float("-infinity")
            Bright = B[mid_for_B + 1] if (mid_for_B + 1) < len(B) else float("infinity")

            if Aleft <= Bright and Bleft <= Aright:
                if total % 2:
                    return min(Aright, Bright)
                return (max(Aleft, Bleft) + min(Aright, Bright)) / 2

            elif Aleft > Bright:
                high = mid_for_A - 1

            else:
                low = mid_for_A + 1
                

        