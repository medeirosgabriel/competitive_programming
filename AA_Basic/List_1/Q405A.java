package List_1;

import java.io.BufferedReader;
import java.io.IOException;
import java.io.InputStreamReader;
import java.util.Arrays;

public class Q405A { // OK

	public static void main(String[] args) throws IOException {
		BufferedReader in = new BufferedReader(new InputStreamReader(System.in));
		int n = in.read();
		in.readLine();
		int[] data = Arrays.stream(in.readLine().split(" ")).mapToInt(Integer :: parseInt).toArray();
		System.out.println(solution(data));
	}

	private static String solution(int[] data) {
		for (int i = data.length - 1; i >= 0; i--) {
			for (int j = i - 1; j >= 0; j--) {
				if (data[j] > data[i]) {
					int dif = data[j] - data[i];
					data[j] = data[i];
					data[i] += dif;
				}
			}
		}
		return imprimir(data);
	}
	
	private static String imprimir(int[] array) {
		String output = "";
		for (int i = 0; i < array.length; i++) {
			output += array[i] + " ";
		}
		return output.trim();
	}
}
