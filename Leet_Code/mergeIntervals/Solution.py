class Solution(object):
    def merge(self, intervals):
        """
        :type intervals: List[List[int]]
        :rtype: List[List[int]]
        """
        intervals.sort()
        i = intervals[0]
        start, end = i[0], i[1]
        result = []
        for inte in intervals[1:]:
            s, e = inte[0], inte[1]
            if (s >= start and s <= end):
                end = max(end, e)
            else:
                result.append([start, end])
                start, end = s, e
        result.append([start, end])
        return result
