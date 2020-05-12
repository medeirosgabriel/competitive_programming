package List_2;

import java.io.BufferedReader;
import java.io.IOException;
import java.io.InputStreamReader;
import java.util.Arrays;

public class Q1141A { // OK
	public static void main(String[] args) throws IOException {
		BufferedReader in = new BufferedReader(new InputStreamReader(System.in));
		long[] data = Arrays.stream(in.readLine().split(" ")).mapToLong(Long::parseLong).toArray();
		System.out.println(solution(data));
	}

	private static long solution(long[] data) {
		if (data[1] % data[0] != 0) {
			return -1;
		}else {
			long n = data[1]/data[0];
			int count = 0;
			while (n != 1) {
				if (n%2 == 0) {
					n = n/2;
					count += 1;
				}else if (n%3 == 0) {
					n = n/3;
					count += 1;
				}else {
					return -1;
				}
			}
			return count;
		}
	}
}
