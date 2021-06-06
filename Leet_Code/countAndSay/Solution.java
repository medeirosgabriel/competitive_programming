class Solution {

	public static String countAndSay(int n) {

		String out = "1";

		if (n > 1) {

			for (int i = 0; i < n; i++) {

				String curr = out;
				int size = curr.length();
				out = "";
				char cword = ' ';
				int count = 0;

				System.out.println(curr);

				for (int j = 0; j < size; j++) {

					boolean flag = false;
					char nword = curr.charAt(j);
					cword = (cword == ' ') ? nword : cword;
					count += (nword == cword) ? 1 : 0;

					if (nword != cword) {
						
						out += Integer.toString(count);
						out += Character.toString(cword);
						cword = nword;
						count = 1;

						if (j == size - 1) {

							out += Integer.toString(count);
							out += Character.toString(cword);
						
						}

					} else {

						if (j == size - 1) {

							out += Integer.toString(count);
							out += Character.toString(cword);

						}
					}
				}
			}
		}

		return out;

	}
}
