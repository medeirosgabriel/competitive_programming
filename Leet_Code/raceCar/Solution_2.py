class Solution(object):
    def racecar(self, target):
        """
        :type target: int
        :rtype: int
        """
        queue = collections.deque([(0, 0, 1)])
        while queue:
            moves, pos, speed = queue.popleft()
            if pos == target: return moves
            queue.append((moves + 1, pos + speed, speed * 2))
            if (pos + speed > target and speed > 0) or (pos + speed < target and speed < 0):
                new_speed = -1 if speed > 0 else 1
                queue.append((moves + 1, pos, new_speed))
        return 0
