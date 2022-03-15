########## First Solution #########

class Solution(object):
    def maximalRectangle(self, matrix):
        """
        :type matrix: List[List[str]]
        :rtype: int
        """
        
        heights = []
        
        for i in range(len(matrix)):
            heights.append([0] * len(matrix[0]))
            
        max_area = 0
        
        for i in range(len(matrix)):
            for j in range(len(matrix[i])):
                heights[i][j] = int(matrix[i][j])
                if (i > 0):
                    if (heights[i][j] != 0):
                        heights[i][j] += heights[i - 1][j]
                        
            values = list(set(heights[i]))
            values.sort()
            
            areas = []
            for v in values:
                c = 0
                for e in heights[i]:
                    if (e != 0 and e >= v):
                        c += 1
                    else:
                        areas.append(c * v)
                        c = 0
                areas.append(c * v)
            
            max_area = max(max_area, max(areas))
            
        return max_area


######### Second Solution #########


class Solution(object):
    def maximalRectangle(self, matrix):
        """
        :type matrix: List[List[str]]
        :rtype: int
        """
        
        heights = []
        
        for i in range(len(matrix)):
            heights.append([0] * len(matrix[0]))
            
        max_area = 0
        
        for i in range(len(matrix)):
            
            for j in range(len(matrix[i])):
                heights[i][j] = int(matrix[i][j])
                if (i > 0):
                    if (heights[i][j] != 0):
                        heights[i][j] += heights[i - 1][j]
            
            stack = []
            
            for j, h in enumerate(heights[i]):
                start = j
                while (len(stack) > 0 and stack[-1][1] > h):
                    index, height = stack.pop()
                    max_area = max(max_area, height * (j - index))
                    start = index
                stack.append((start, h))
                
            for j, h in stack:
                max_area = max(max_area, h * (len(heights[i]) - j))
            
        return max_area
        
