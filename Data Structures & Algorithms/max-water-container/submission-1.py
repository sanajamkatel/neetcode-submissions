class Solution:
    def maxArea(self, heights: List[int]) -> int:
        result = 0
        for left in range(len(heights)):
            for right in range(left+1, len(heights)):
                distance = right - left
                stored_water = min(heights[left], heights[right])
                total_water_stored = distance * stored_water
                result = max(result,total_water_stored )

        return result
        