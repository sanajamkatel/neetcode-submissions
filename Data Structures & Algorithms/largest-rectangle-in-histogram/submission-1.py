class Solution:
    def largestRectangleArea(self, heights: List[int]) -> int:
        stack = []
        n = len(heights)
        leftside = [-1] * n
        max_area = 0

        for i in range(n):
            while stack and heights[stack[-1]] >= heights[i]:
                stack.pop()

            if stack:
                leftside[i] = stack[-1]

            stack.append(i)

        stack = []
        rightside = [n] * n
        for i in range(n-1, -1,-1):
            while stack and heights[stack[-1]] >= heights[i]:
                stack.pop()

            if stack:
                rightside[i] = stack[-1]

            stack.append(i)


        for i in range(n):
            leftside[i] += 1
            rightside[i] -= 1
            max_area = max(max_area, (rightside[i]-leftside[i] +1) * heights[i] )
        
        return max_area

        