class Solution(object):
    def fractionToDecimal(self, n, d):
        """
        :type n: int
        :type d: int
        :rtype: str
        """
        if n == 0: return "0"

        negative = (n < 0) != (d < 0)
        n, d = abs(n), abs(d)
        sol = str(n // d)
        dec = ""
        
        if n % d > 0:
            nums = {}
            sol += "."
            n = n % d
            while (n > 0):
                if n in nums:
                    dec += ")"
                    pos = nums[n]
                    dec = dec[:pos] + "(" + dec[pos:]
                    break
                
                nums[n] = len(dec)
                n *= 10
                dec += str(n // d)
                n = n % d
                
        sign = "-" if negative else ""
        return sign + sol + dec
