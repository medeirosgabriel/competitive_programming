class Solution(object):
    def longestPalindrome(self, s):
        """
        :type s: str
        :rtype: int
        """
        counter = {}
        for c in s:
            if (not c in counter):
                counter[c] = 0
            counter[c] += 1
        result = 0
        rest = False
        for k in counter.keys():
            result += int(counter[k]/2) * 2
            rest = rest or (True if(counter[k] % 2 != 0) else False)
        return result + (1 if rest else 0)
