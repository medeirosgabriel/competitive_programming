class Solution(object):
    def maximumRobots(self, chargeTimes, runningCosts, budget):
        """
        :type chargeTimes: List[int]
        :type runningCosts: List[int]
        :type budget: int
        :rtype: int
        """
        dq = deque()
        left, running_sum, answer = 0, 0, 0
        for right in range(len(chargeTimes)):
            running_sum += runningCosts[right]
            while dq and chargeTimes[dq[-1]] < chargeTimes[right]:
                dq.pop()
            dq.append(right)
            while dq and chargeTimes[dq[0]] + running_sum * (right - left + 1) > budget:
                if (dq[0] == left):
                    dq.popleft()
                running_sum -= runningCosts[left]
                left += 1
            answer = max(answer, right - left + 1)
        return answer
