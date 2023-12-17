class Solution(object):
    def longestCommonPrefix(self, strs):
        """
        :type strs: List[str]
        :rtype: str
        """
        ret, strs = "", sorted(strs)
        i = 0
        while (i < len(strs[0])):
            c = strs[0][i]
            for s in strs:
                if (i < len(s) and s[i] == c):
                    continue
                else:
                    return ret
            ret += c
            i += 1
        return ret

