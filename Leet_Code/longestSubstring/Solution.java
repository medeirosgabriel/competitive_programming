public class Solution {

	public static int lengthOfLongestSubstring(String s) {

		int[] hash = new int[130];
		int cc = 0, rc = -1;

		for (int i = 0; i < s.length(); i++) {
			char c = s.charAt(i);
			int index = (int) c;
			if (hash[index] == 0) {
				hash[index] ++;
				cc ++;		
			} else {
				if (cc > rc) {
					rc = cc;
				}
				hash = new int[130];
				cc = 1;
			}
		}

		if (cc > rc) {
			rc = cc;
		}

		return rc;
	}
}
