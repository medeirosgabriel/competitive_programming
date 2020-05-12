package List_1;

import java.io.BufferedReader;
import java.io.IOException;
import java.io.InputStreamReader;

public class Q981A { // OK
	
	public static void main(String[] args) throws IOException {
		BufferedReader in = new BufferedReader(new InputStreamReader(System.in));
		String word = in.readLine();
		if (word.length() == 1) {
			System.out.println(0);
		}else{
			System.out.println(solution(word));
		}
	}
	
	public static int solution(String word) throws IOException {
		int i = 0;
		int j = word.length() - 1;
		boolean equals = true;
		while (i <= j) {
			if (word.charAt(i) == word.charAt(j)) {
				i ++;
				j --;
				if (word.charAt(i) != word.charAt(0) || word.charAt(j) != word.charAt(0)) {
					equals = false;
				}
			}else {
				return word.length();
			}
		}
		return (equals) ? 0 : word.length() - 1;
	}
}