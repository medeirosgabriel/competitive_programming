package List_2;

import java.io.BufferedReader;
import java.io.IOException;
import java.io.InputStreamReader;

public class Q954A { //OK
	
	public static void main(String[] args) throws IOException {
		BufferedReader in = new BufferedReader(new InputStreamReader(System.in));
		int n = in.read();
		in.readLine();
		String str = in.readLine();
		System.out.println(solution(str));
	}

	private static int solution(String str) {
		int i = 0, cont = 0;
		while (i <= str.length() - 1) {
			if (i + 1 <= str.length() - 1 && str.charAt(i) != str.charAt(i + 1)) {
					cont += 1;
					i += 2;
			}else {
				i += 1;
			}
		}
		return str.length() - cont;
	}
}
