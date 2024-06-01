from collections import deque

class Solution(object):
    def racecar(self, target):
        """
        :type target: int
        :rtype: int
        """
        q = deque([(0, 1, 0)]) # position, speed, length
        visited = set()
        visited.add((0,1)) # speed, length
        while (q):
            p, s, l = q.popleft()
            if (p == target): 
                return l
                
            if ((p + s, s * 2) not in visited):
                q.append((p + s, s * 2, l + 1))
                visited.add((p + s, s * 2))

            ns = -1 if s > 0 else 1
            if ((p, ns) not in visited):
                q.append((p, ns, l + 1))
                visited.add((p, ns))
