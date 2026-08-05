class Solution(object):
    def twoSum(self, numbers, target):
        """
        :type numbers: List[int]
        :type target: int
        :rtype: List[int]
        """
        n = len(numbers)
        p1, p2 = 0, n - 1,
        while (p2 < n):
            n1, n2 = numbers[p1], numbers[p2]
            if (n1 + n2 == target):
                return [p1 + 1, p2 + 1]
            elif (n1 + n2 < target):
                p1 += 1
            else:
                p2 -= 1
        return [p1 + 1, p2 + 1]
