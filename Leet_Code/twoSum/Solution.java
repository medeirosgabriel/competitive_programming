package twoSum;

import java.util.Arrays;
import java.util.HashMap;
import java.util.Map;

public class Solution {
	public static void main(String[] args) {
		String out = Arrays.toString(twoSum(new int[] {3,2,4}, 6));
		System.out.println(out);
	}
	
	private static int[] twoSum(int[] nums, int target) {
        Map<Integer, Integer> numbers = new HashMap<>();
        
        for (int i = 0; i < nums.length; i++) {
        	numbers.put(nums[i], i);
        }
        
        for (int i = 0; i < nums.length; i++) {
        	int c = target - nums[i];
        	if (numbers.containsKey(c) && numbers.get(c) != i) {
        		return new int[] {i , numbers.get(c)};
        	}
        }
        
        throw new IllegalArgumentException("No solution");
    }
}
