package List_2;

import java.io.BufferedReader;
import java.io.IOException;
import java.io.InputStreamReader;
import java.util.Arrays;

public class Q723A { //OK
	
	public static void main(String[] args) throws IOException {
		BufferedReader in = new BufferedReader(new InputStreamReader(System.in));
		int[] array = Arrays.stream(in.readLine().split(" ")).mapToInt(Integer :: parseInt).toArray();
		int max = Arrays.stream(array).max().getAsInt();
		int min = Arrays.stream(array).min().getAsInt();
		int output = Integer.MAX_VALUE;
		while (min <= max) {
			int temp = 0;
			for (int i = 0; i < array.length; i++) {
				temp += Math.abs(array[i] - min);
			}
			if (temp < output) {
				output = temp;
			}
			min++;
		}
		System.out.println(output);
	}
}
