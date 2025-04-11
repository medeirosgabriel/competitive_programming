class Solution {
    public int[] searchRange(int[] nums, int target) {
        if (nums.length > 0) {
            int left = leftIndex(nums, target);
            int right = rightIndex(nums, target);
            return new int[]{left, right};
        }
        return new int[]{-1, -1};
    }

    public int leftIndex(int[] nums, int target) {
        int left = 0, right = nums.length - 1, mid;
        while (left <= right) {
            mid = (left + right)/2;
            if (target <= nums[mid]) {
                right = mid - 1;
            } else {
                left = mid + 1;
            }
        }
        return (left < nums.length && nums[left] == target) ? left : -1;
    }

    public int rightIndex(int[] nums, int target) {
        int left = 0, right = nums.length - 1, mid;
        while (left <= right) {
            mid = (left + right)/2;
            if (target >= nums[mid]) {
                left = mid + 1;
            } else {
                right = mid - 1;
            }
        }
        return (right > -1 && nums[right] == target) ? right : -1;
    }
}
