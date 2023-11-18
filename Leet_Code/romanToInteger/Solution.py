class Solution(object):
    def romanToInt(self, s):
        """
        :type s: str
        :rtype: int
        """
        value = {"I": 1, "V": 5, "X": 10, "L": 50, "C": 100, "D": 500, "M": 1000}
        n, i, aux = 0, 0, 0
        last = -1
        while (i < len(s)):
            v1 = value[s[i]]
            if (i + 1 < len(s)):
                v2 = value[s[i + 1]]
                if (v1 < v2):
                    aux += v1
                else:
                    n += (v1 - aux)
                    aux = 0
            else:
                if (v1 <= last):
                    n += (v1 + aux)
                else:
                    n += (v1 - aux)
            last = v1
            i += 1

        return n
