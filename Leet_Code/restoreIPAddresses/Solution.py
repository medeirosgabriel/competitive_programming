class Solution(object):
    def restoreIpAddresses(self, s):
        """
        :type s: str
        :rtype: List[str]
        """
        self.result = []
        def backtracking(curr, count, s):
            if (count < 4 and s != ""):
                for i in range(1, 4):
                    temp = s[0:i]
                    if (len(temp) > 1 and s[0] == "0"): 
                        return
                    n = int(temp)
                    if (n <= 255):
                        if (curr != ""):
                            backtracking(curr + "." + temp, count + 1, s[i:])
                        else:
                            backtracking(temp, count + 1, s[i:])

            elif (count == 4 and len(curr) - 3 == self.n):
                if (not curr in self.result):
                    self.result.append(curr)
        
        self.n = len(s)
        backtracking("", 0, s)
        return self.result
        
