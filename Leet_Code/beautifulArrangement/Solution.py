class Solution:
    def backtracking(self, index):
        if (index > self.n): return 1
        count = 0
        for i in range(1, self.n + 1):
            if (not self.visited[i] and (i % index == 0 or index % i == 0)):
                self.visited[i] = True
                count += self.backtracking(index + 1)
                self.visited[i] = False
        return count

    def countArrangement(self, n: int) -> int:
        self.visited = [False] * (n + 1)
        self.n = n
        return self.backtracking(1)
