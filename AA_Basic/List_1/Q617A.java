package List_1;

import java.util.Scanner;

public class Q617A { // OK

	public static void main(String[] args) {
		Scanner input = new Scanner(System.in);
		int n = input.nextInt();
		input.nextLine();
		System.out.println(solution(n));
	}

	private static int solution(int n) {
		int times = 0;
		for (int i = 5; i >= 1; i--) {
			times += (n/i);
			n = n%i;
		}
		return times;
	}
}
