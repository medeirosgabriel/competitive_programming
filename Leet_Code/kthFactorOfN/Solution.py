class Solution(object):
    def kthFactor(self, n, k):
        """
        :type n: int
        :type k: int
        :rtype: int
        """
        factors = []
        for i in range(1, n + 1):
            if (n % i == 0):
                factors.append(i)

        return -1 if k - 1 >= len(factors) else factors[k - 1]
