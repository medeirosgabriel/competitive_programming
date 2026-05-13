class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        nums_set, max_seq = set(nums), 0
        for n in nums_set:
            count = 0
            if (not n - 1 in nums_set):
                count += 1
                n += 1
                while n in nums_set:
                    n += 1
                    count += 1
                max_seq = max(max_seq, count)
        return max_seq

