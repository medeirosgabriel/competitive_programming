class Solution(object):
    def removeDuplicates(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        i = 0
        n_set = set()
        for n in nums:
            if (not n in n_set):
                n_set.add(n)
                nums[i] = n
                i += 1
        return i
