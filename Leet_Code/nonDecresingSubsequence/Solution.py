class Solution:
    def backTracking(self, array, nums):
        if (len(array) >= 2 and (not tuple(array) in self.result)): 
            self.result.add(tuple(array))
        if (nums):
            for i in range(len(nums)):
                n = nums[i]
                if (array):
                    if (n >= array[-1]):
                        self.backTracking(array + [n], nums[i + 1:])
                    else:
                        self.backTracking(array, nums[i + 1:])
                else:
                    self.backTracking([n], nums[i + 1:])


    def findSubsequences(self, nums: List[int]) -> List[List[int]]:
        self.result = set()
        self.backTracking([], nums)
        return list(self.result)
