class Solution(object):
    def backtracking(self, curr, digits):
        if (not digits):
            self.result.append(curr)
            return
        d = digits[0]
        for n in self.keyboard[d]:
            self.backtracking(curr + n, digits[1:])

    def letterCombinations(self, digits):
        """
        :type digits: str
        :rtype: List[str]
        """
        if not digits: return []
        self.keyboard = {
            "2": "abc",
            "3": "def",
            "4": "ghi",
            "5": "jkl",
            "6": "mno",
            "7": "pqrs",
            "8": "tuv",
            "9": "wxyz"
        }
        self.result = []
        self.backtracking("", digits)
        return self.result
