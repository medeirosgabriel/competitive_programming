class Solution(object):
    def myAtoi(self, s):
        """
        :type s: str
        :rtype: int
        """
        sig, number = "", ""
        flag = False
        for i in range(len(s)):
            n = s[i]
            if (n == " "):
                if (number != "" or sig != ""): flag = True
                continue
            elif (n.isnumeric()):
                if (flag): break
                number += n
            elif (n in "+-"):
                if (flag): break
                if (sig != "" or number != ""): break
                sig = n
            else: break

        ret, n = 0, len(number)
        for i in range(len(number)):
            ret += int(number[i]) * pow(10, n - i - 1)
        
        ret = -ret if sig == "-" else ret

        INT_MIN, INT_MAX = -(2**31), 2**31 - 1
        if ret < INT_MIN: 
            return INT_MIN
        elif ret > INT_MAX: 
            return INT_MAX
        else: return ret
