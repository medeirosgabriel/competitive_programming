class Solution {
	
	public static int rob(int[] nums) {
        	
		int r = -1, start = 0;
		
		for (int i = 0; i < 2; i++) {
			int sum  = nums[start], j = start + 2;

			do {
				sum += nums[j];
				j += 2;
				j %= nums.length;
			} while (j%(nums.length - 1) != start + 1 
					&& j%(nums.length - 1) != start);

			r = (sum > r) ? sum : r;
			start ++;
		}

		return r;
	}
}
