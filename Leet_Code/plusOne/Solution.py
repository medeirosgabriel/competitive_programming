class Solution(object):
    def recursion(self, digits, index, sum_):
        if (index >= 0):
            if (digits[index] + sum_ >= 10):
                digits[index] = (digits[index] + sum_) % 10
                self.recursion(digits, index - 1, 1)
            else:
                digits[index] = digits[index] + sum_
        else:
            digits.insert(0, 1)

    def plusOne(self, digits):
        """
        :type digits: List[int]
        :rtype: List[int]
        """
        self.recursion(digits, len(digits) - 1, 1)
        return digits
