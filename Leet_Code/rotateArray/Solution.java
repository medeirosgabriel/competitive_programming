public class Solution {
	
	public static void rotate(int[] nums, int k) {
		int size = nums.length;
		int[] flags = new int[size];
		int s = 0, i = k, n = nums[0], temp;
		while (s < size) {
			if (flags[i] == 0) {
				s++;
				temp = n;
				n = nums[i];
				nums[i] = temp;
				flags[i] = 1;
				i = (i + k) % size;
			} else {
				i = (i + 1) % size;
				n = nums[i];
				i = (i + k) % size;
			}
		}
	}
}
