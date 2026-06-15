class Solution:
    def maxArea(self, heights: List[int]) -> int:
        # result = 0
        # for left in range(len(heights)):
        #     for right in range(left+1, len(heights)):
        #         distance = right - left
        #         stored_water = min(heights[left], heights[right])
        #         total_water_stored = distance * stored_water
        #         result = max(result,total_water_stored )

        # return result
        tapped_water = 0
        left = 0
        right = len(heights) - 1
        while left < right:
            total_water_stored = (right-left) * min(heights[left], heights[right])
            tapped_water = max(tapped_water, total_water_stored)

            if heights[left] < heights[right]:
                left += 1

            else:
                right -= 1

            

        return tapped_water

        