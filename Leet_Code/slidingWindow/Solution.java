class Solution {
	
	public static int[] maxSlidingWindow(int[] nums, int k) {
        	
		int[] output = new int[nums.length - k + 1]; 
		
		int index = 0, hi = -1, highest = -100000;

		for (int i = 0; i < k; i++) {
			if (highest < nums[i]) {
				highest = nums[i];
				hi = i;
				output[index] = highest;
			}
		}

		index++;

		int p1 = 1, p2 = k;

		while (p2 < nums.length) {
			if (hi > p1 && hi < p2) {
				if (highest < nums[p2]) {
					highest = nums[p2];
					hi = p2;
				}
			} else {
				for (int i = p1; i <= p2; i++) {
					if (highest < nums[i]) {
						highest = nums[i];
						hi = i;
					}
				}
			}
			output[index++] = highest;
			p2++; p1++;
		}

		return output;
	}
}
