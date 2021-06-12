import java.util.Arrays;
class Solution {
	
	public static boolean containsNearbyAlmostDuplicate(int[] nums, int k, int t) {
		int[] indexes = new int[100000];
		for (int i = 0; i < 100000; i++) {indexes[i] = i;}
        	quickSort(nums, indexes, 0, nums.length - 1);
		System.out.println(Arrays.toString(nums) + " " + Arrays.toString(indexes));
		boolean r = false;
		int i = 0;
		while (i < nums.length - 1 && !r) {
			int a = nums[i], b = nums[i + 1];
			r = Math.abs(a - b) <= t && Math.abs(indexes[i] - indexes[i + 1]) <= k;
			i ++;
		}
		return r;
	}

	private static void quickSort(int[] nums, int[] indexes, int start, int end) {
		if (start < end) {
			int pivotPosition = partition(nums, indexes, start, end);
			quickSort(nums, indexes, start, pivotPosition - 1);
			quickSort(nums, indexes, pivotPosition + 1, end);
		}
	}

	private static int partition(int[] nums, int[] indexes, int start, int end) {
		int pivot = nums[start];
		int p1 = start, p2 = end;
		while (p1 <= p2) {
			if (nums[p1] <= pivot) {
				p1 ++;
			} else if (nums[p2] > pivot) {
				p2 --;
			} else {
				int temp = nums[p1];
				nums[p1] = nums[p2]; nums[p2] = temp;
				temp = indexes[p1];
				indexes[p1] = indexes[p2]; indexes[p2] = temp;
			}
		}
		indexes[start] = indexes[p2];
		indexes[p2] = start;
		nums[start] = nums[p2];
		nums[p2] = pivot;
		return p2;
	}
}
