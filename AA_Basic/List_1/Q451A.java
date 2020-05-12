package List_1;

import java.io.BufferedReader;
import java.io.IOException;
import java.io.InputStreamReader;
import java.util.Arrays;

public class Q451A { // OK

	public static void main(String[] args) throws IOException {
		BufferedReader in = new BufferedReader(new InputStreamReader(System.in));
		int[] data = Arrays.stream(in.readLine().split(" ")).mapToInt(Integer :: parseInt).toArray();
		System.out.println(solution(data));
	}
	
	public static String solution(int[] array) {
		int min = array[0];
		if (array[0] > array[1]) {
			min = array[1];
		}
		if (min % 2 == 0) {
			return "Malvika";
		}else {
			return "Akshat";
		}
	}

}
