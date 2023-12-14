class Solution(object):
    def partitionString(self, s):
        """
        :type s: str
        :rtype: int
        """
        result = 1
        aux = ''
        for c in s:
            if (c in aux):
                aux = c
                result += 1
            else:
                aux += c
        return result
