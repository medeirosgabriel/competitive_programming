package kruskal;

import java.util.Comparator;

public class PQComparator implements Comparator<int[]> {

	@Override
	public int compare(int[] arg0, int[] arg1) {
		if (arg0[2] < arg1[2]) {
            return -1;
		} else {
            return 1;
        }
	}
}
