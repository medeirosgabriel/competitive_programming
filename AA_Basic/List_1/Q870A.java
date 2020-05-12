package List_1;

import java.io.BufferedReader;
import java.io.IOException;
import java.io.InputStreamReader;
import java.util.Arrays;

public class Q870A { //OK
	
	public static void main(String[] args) throws IOException {
		BufferedReader in = new BufferedReader(new InputStreamReader(System.in));
		String[] sizes = in.readLine().split(" ");
		int[] l1 = Arrays.stream(in.readLine().split(" ")).mapToInt(Integer::parseInt).toArray();
		int[] l2 = Arrays.stream(in.readLine().split(" ")).mapToInt(Integer::parseInt).toArray();
		System.out.println(solution(l1, l2));
	}

	private static String solution(int[] l1, int[] l2) {
		int n = 11;
		for (int i = 0; i < l1.length; i++) {
			for (int j = 0; j < l2.length; j++) {
				if (l1[i] == l2[j] && l1[i] < n) {
					n = l1[i];
				}
			}
		}
		if (n != 11) {
			return n + "";
		}else{
			int min = Arrays.stream(l1).min().getAsInt();
			int min2 = Arrays.stream(l2).min().getAsInt();
			if (min != min2) {
				if (min < min2) {
					return min + "" + min2;
				}else{
					return min2 + "" + min;
				}
			}else{
				return min + "";
			}
		}
	}
}
