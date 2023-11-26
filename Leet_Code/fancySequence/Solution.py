class Fancy(object):

    def __init__(self):
        self.nums = []
        self.inc = [0]
        self.mult = [1]

    def append(self, val):
        """
        :type val: int
        :rtype: None
        """
        self.nums.append(val)
        self.inc.append(self.inc[-1])
        self.mult.append(self.mult[-1])
        

    def addAll(self, inc):
        """
        :type inc: int
        :rtype: None
        """
        self.inc[-1] += inc
        

    def multAll(self, m):
        """
        :type m: int
        :rtype: None
        """
        self.mult[-1] *= m
        self.inc[-1] *= m
        

    def getIndex(self, idx):
        """
        :type idx: int
        :rtype: int
        """
        if (idx >= len(self.nums)):
            return -1
        mult = self.mult[-1] // self.mult[idx]
        inc = self.inc[-1] - self.inc[idx] * mult
        mod = 10 ** 9 + 7
        return (self.nums[idx] * mult + inc) % mod
        


# Your Fancy object will be instantiated and called as such:
# obj = Fancy()
# obj.append(val)
# obj.addAll(inc)
# obj.multAll(m)
# param_4 = obj.getIndex(idx)
