package List_2;

import java.util.Arrays;
import java.util.Scanner;

public class Q200B { //OK

	public static void main(String[] args) {
		Scanner input = new Scanner(System.in);
		int n = input.nextInt();
		input.nextLine();
		int[] array = Arrays.stream(input.nextLine().split(" ")).mapToInt(Integer :: parseInt).toArray();
		float p = 0;
		for (int i = 0; i < array.length; i++) {
			p += array[i]/100.0;
		}
		p*=100;
		System.out.printf("%.5f", p/n);
	}
}
