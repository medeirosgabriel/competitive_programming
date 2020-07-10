package List_2;

import java.io.BufferedReader;
import java.io.IOException;
import java.io.InputStreamReader;

public class Q1141B { // OK

	public static void main(String[] args) throws IOException {
		BufferedReader in = new BufferedReader(new InputStreamReader(System.in));
		int n = in.read();
		in.readLine();
		String[] data = in.readLine().split(" ");
		solution(data);
	}

	private static void solution(String[] array) {
		int max = -1, temp = 0, first = 0;
		boolean flag = true;
		for (int i = 0;  i < array.length; i++) {
			if (array[i].equals("1")) {
				temp += 1;
				if (flag) {
					first += 1;
				}
			}else {
				if (temp > max) {
					max = temp;
				}
				flag = false;
				temp = 0;
			}
		}
		if (max == -1) {
			System.out.println(temp);
		}else if (temp + first > max) {
			System.out.println(temp + first);
		}else {
			System.out.println(max);
		}
	}
}
