import java.util.Arrays;

public class Test {
	
	public static void main(String[] args) {
		
		int[] input = new int[]{9,11};
		int[] output = Solution.maxSlidingWindow(input, 2);
		System.out.println(Arrays.toString(output));
	
	}
}
