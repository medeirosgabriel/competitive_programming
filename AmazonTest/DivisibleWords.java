public class DivisibleWords {
	
	public static void main(String[] args) {

		String principal = args[0];
		String substring = args[1];

		System.out.println(isDivisible(principal, substring));
		
	}

	public static int isDivisible(String principal, String substring) {

		int len = substring.length();

		for (int i = 0; i < principal.length(); i++) {

			if (substring.charAt(i % len) != principal.charAt(i)) {

				return -1;

			}
		}

		for (int i = 0; i < substring.length(); i++) {
			
			String sub = substring.substring(0, i + 1);

			len = sub.length();

			for (int j = 0; j < substring.length(); j++) {

				if (sub.charAt(j % len) != substring.charAt(j)) {

					break;

				} else {

					if (j == substring.length() - 1) {

						return len;

					}
				}
			}
			
		}

		return substring.length();
	}
}

