public class Solution {

	public static void main(String[] args) {
		int[] nums = {1,3,5,6};
		int target = 7;
		System.out.println(searchInsert(nums, target));
	}

	public static  int searchInsert(int[] nums, int target) {
		int mid, n, left = 0, right = nums.length - 1;
		while (left < right) {
			mid = (left + right)/2;
			n = nums[mid];
			if (target <= n) {
				right = mid - 1;
			} else {
				left = mid + 1;
			}
		}
		if (left == right) {
			return (nums[left] < target) ? left + 1 : left;
		}
        return left;
    }
}
