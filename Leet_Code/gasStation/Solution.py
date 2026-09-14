class Solution(object):
    def canCompleteCircuit(self, gas, cost):
        """
        :type gas: List[int]
        :type cost: List[int]
        :rtype: int
        """
        if sum(gas) < sum(cost): return -1
        curr_gas, start, n = 0, 0, len(gas)
        for i in range(n):
            curr_gas += gas[i] - cost[i]
            if (curr_gas < 0):
                curr_gas = 0
                start = i + 1
        return start
        
