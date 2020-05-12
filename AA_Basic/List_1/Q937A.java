package List_1;

import java.io.BufferedReader;
import java.io.IOException;
import java.io.InputStreamReader;
import java.util.Arrays;
import java.util.stream.Stream;

public class Q937A { // OK

	public static void main(String[] args) throws IOException {
		BufferedReader in = new BufferedReader(new InputStreamReader(System.in));
		int n = in.read();
		in.readLine();
		int[] data = Stream.of(in.readLine().split(" ")).mapToInt(Integer :: parseInt).toArray();
		int max = Arrays.stream(data).max().getAsInt();
		boolean[] aux = new boolean[max + 1];
		int cont = 0;
		for (int i = 0; i < data.length; i++) {
			if (!aux[data[i]] && data[i] != 0) {
				cont ++;
				aux[data[i]] = true;
			}
		}
		System.out.println(cont);
	}

}
