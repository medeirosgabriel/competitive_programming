from collections import Counter

class Solution(object):
    def minWindow(self, s, t):
        """
        :type s: str
        :type t: str
        :rtype: str
        """
        occ = Counter(t)
        required, min_len = len(t), float('inf')
        l, start = 0, 0
        for r in range(len(s)):
            if s[r] in occ:
                occ[s[r]] -= 1
                if occ[s[r]] >= 0:
                    required -= 1
            while required == 0:
                if r - l + 1 < min_len:
                    min_len = r - l + 1
                    start = l
                if s[l] in occ:
                    occ[s[l]] += 1
                    if occ[s[l]] > 0:
                        required += 1
                l += 1
        return s[start:start + min_len] if min_len != float('inf') else ""

