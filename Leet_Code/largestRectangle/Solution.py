class Solution(object):
    def largestRectangleArea(self, heights):
        """
        :type heights: List[int]
        :rtype: int
        """
        n, max_area = len(heights), 0
        stack = []
        for i in range(n + 1):
            curr_h = heights[i] if i < n else 0
            while stack and curr_h < heights[stack[-1]]:
                height = heights[stack.pop()]
                width = i if not stack else i - stack[-1] - 1
                max_area = max(max_area, width * height)
            stack.append(i)
        return max_area

