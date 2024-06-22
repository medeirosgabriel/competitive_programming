class Solution(object):
    def multiply(self, num1, num2):
        """
        :type num1: str
        :type num2: str
        :rtype: str
        """
        n1, n2 = list(num1), list(num2)
        n1.reverse()
        n2.reverse()
        e1, s1 = 1, 0
        e2, s2 = 1, 0

        for n in n1:
            n = int(n)
            s1 += e1 * n
            e1 *= 10
        
        for n in n2:
            n = int(n)
            s2 += e2 * n
            e2 *= 10

        return str(s1 * s2)
