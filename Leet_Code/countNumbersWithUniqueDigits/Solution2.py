class Solution:

    def countNumbersWithUniqueDigits(self, n: int) -> int:
        if (n == 0): return 1
        res, unique, remain = 10, 9, 9
        for i in range(2, n + 1):
            unique *= remain
            res += unique
            remain -= 1
        return res
