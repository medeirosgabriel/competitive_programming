package List_2;

import java.io.BufferedReader;
import java.io.IOException;
import java.io.InputStreamReader;
import java.util.Arrays;

public class Q160A { // OK
	
	public static void main(String[] args) throws IOException {
		BufferedReader in = new BufferedReader(new InputStreamReader(System.in));
		int n = in.read();
		in.readLine();
		int[] data = Arrays.stream(in.readLine().split(" "))
				.mapToInt(Integer :: parseInt).toArray();
		solution(data);
	}
	
	private static void solution(int[] data) {
		quickSort(data, 0, data.length - 1);
		int sum = Arrays.stream(data).sum();
		int my = 0;
		int i = 0;
		while (my <= sum && i <= data.length - 1) {
			my += data[i];
			sum -= data[i];
			i++;
		}
		System.out.println(i);;
	}

	public static void quickSort(int[] array, int start, int f) {
		if (start < f) {
			int pivotPosition = partition(array, start, f);
			quickSort(array, start, pivotPosition - 1);
			quickSort(array, pivotPosition + 1, f);
		}
	}

	private static int partition(int[] array, int start, int f) {
		int pivot = array[start], left = start, right = f, temp;
		while (left <= right) {
			if (array[left] >= pivot) {
				left ++;
			}else if (array[right] < pivot) {
				right --;
			}else {
				temp = array[left];
				array[left] = array[right];
				array[right] = temp;
			}
		}
		array[start] = array[right];
		array[right] = pivot;
		return right;
	}
}
