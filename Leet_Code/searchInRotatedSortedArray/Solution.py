class Solution(object):

    """
    def findPivot(self, nums):
        left = 0
        right = len(nums) - 1
        while (left < right):
            mid = (right + left) // 2
            if (nums[mid] > nums[right]):
                left = mid + 1
            else:
                right = mid
        return left

    def binary_search(self, arr, left, right, x):
        if right >= left:
            mid = (right + left) // 2
            print(left, mid, right)
            if arr[mid] == x:
                return mid
            elif arr[mid] > x:
                return self.binary_search(arr, left, mid - 1, x)
            else:
                return self.binary_search(arr, mid + 1, right, x)
        else:
            return -1
    """

    def binary_search(self, array, left, right, target):
        if (left > right): return -1
        else:
            mid = (left + right) // 2
            if (target == array[mid]): return mid
            elif (array[left] <= array[mid]):
                if (array[left] <= target < array[mid]):
                    return self.binary_search(array, left, mid - 1, target)
                else:
                    return self.binary_search(array, mid + 1, right, target)
            else:
                if (array[right] >= target > array[mid]):
                    return self.binary_search(array, mid + 1, right, target)
                else:
                    return self.binary_search(array, left, mid - 1, target)

            

    def search(self, nums, target):
        """
        :type nums: List[int]
        :type target: int
        :rtype: int
        """
        index = self.binary_search(nums, 0, len(nums) - 1, target)
        return index
