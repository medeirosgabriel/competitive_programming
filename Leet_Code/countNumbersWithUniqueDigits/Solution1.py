class Solution:

    def countNumbersWithUniqueDigits(self, n: int) -> int:
        if n == 0: return 1

        def backtracking(number, visited):
            if number == n: return 0
            count = 0
            for i in range(10):
                if i == 0 and len(visited) == 0: continue
                if (not i in visited):
                    visited.append(i)
                    count += 1
                    count += backtracking(number + 1, visited)
                    visited.pop()
            return count

        return 1 + backtracking(0, [])
