import java.util.Arrays;
public class Test {
	public static void main(String[] args) {
		int[] array = new int[]{1,2,2,2,2,3,3,4,5,6,6};
		int n = Integer.parseInt(args[0]);
		int[] r = Solution.searchRange(array, n);
		System.out.println(Arrays.toString(r));
	}
}
