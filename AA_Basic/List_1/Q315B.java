package List_1;

import java.io.BufferedReader;
import java.io.IOException;
import java.io.InputStreamReader;
import java.util.Arrays;

public class Q315B { //OK
	
	public static void main(String[] args) throws IOException {
		BufferedReader in = new BufferedReader(new InputStreamReader(System.in));
		String[] n = in.readLine().split(" ");
		int[] data = Arrays.stream(in.readLine().split(" ")).mapToInt(Integer::parseInt).toArray();
		int s = 0;
		for (int i = 0; i < Integer.parseInt(n[1]); i++) {
			int[] op = Arrays.stream(in.readLine().split(" ")).mapToInt(Integer::parseInt).toArray();
			if (op[0] == 1) {
				data[op[1] - 1] = op[2] - s;
			}else if (op[0] == 2) {
				s += op[1];
			}else {
				System.out.println(data[op[1] - 1] + s);
			}
		}
	}
}
