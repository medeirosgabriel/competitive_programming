public class Solution {
	public static int[] searchRange(int[] nums, int target) {
		int f = floor(nums, 0, nums.length - 1, target);
		int c = ceil(nums, 0, nums.length - 1, target);
		return new int[]{f,c};
	}

	private static int floor(int[] nums, int start, int end, int target) {
		int mid = (start + end)/2;
		if (start <= end) {
			if (nums[mid] < target) {
				return floor(nums, mid + 1, end, target);
			} else {
				return floor(nums, start, mid - 1, target);
			}
		} else {
			return (validIndex(nums.length, start) && nums[start] == target) ? start : -1;
		}
	}

	private static int ceil(int[] nums, int start, int end, int target) {
		int mid = (start + end)/2;
		if (start <= end) {
			if (nums[mid] <= target) {
				return ceil(nums, mid + 1, end, target);
			} else {
				return ceil(nums, start, mid - 1, target);
			}
		} else {
			return (validIndex(nums.length, end) && nums[end] == target) ? end : -1;
		}
	}

	private static boolean validIndex(int size, int index) {
		return index >= 0 && index < size;
	}
}
