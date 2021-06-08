import java.util.Arrays;

class Solution {

	public static String largestNumber(int[] nums) {

		quickSort(nums, 0, nums.length - 1);
		String r = "";
		for (int i = 0; i < nums.length; i++) {
			r += Integer.toString(nums[i]);
		}
		return r;
	}

	private static void quickSort(int[] nums, int start, int end) {
		if (start < end) {
			int pivot  = partition(nums, start, end);
			quickSort(nums, start, pivot - 1);
			quickSort(nums, pivot + 1, end);
		}
	}

	private static int partition(int[] nums, int start, int end) {
		int pivot = nums[start];
		int p1 = start, p2 = end;
		while (p1 <= p2) {
			if (isLargest(nums[p1], pivot)) {
				p1 ++;
			} else if (isLargest(nums[p2], pivot)) {
				int temp = nums[p1];
				nums[p1++] = nums[p2];
				nums[p2--] = temp;
			} else {
				p2 --;
			}
		}
		nums[start] = nums[p2];
		nums[p2] = pivot;
		return p2;
	}

	private static boolean isLargest(int a, int b) {
		
		String as = Integer.toString(a);
		String bs = Integer.toString(b);
		int i = 0;

		while (i < as.length() && i < bs.length()) {
			int ia = (int) as.charAt(i);
			int ib = (int) bs.charAt(i);
			if (ia != ib) { return (ia > ib) ? true : false; }
			i++;
		}

		while (i < as.length()) {
			int ia = (int) as.charAt(i);
			int ib = (int) bs.charAt(0);
			if (ia != ib) { return (ia > ib) ? true : false; }
			i++;
		}

		while (i < bs.length()) {
			int ia = (int) as.charAt(0);
			int ib = (int) bs.charAt(i);
			if (ia != ib) { return (ia > ib) ? true : false; }
			i++;
                }

		return true;

	}
}
