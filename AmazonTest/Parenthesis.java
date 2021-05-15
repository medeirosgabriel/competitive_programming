public class Parenthesis {

	public static void main(String[] args) {

		String sequence = args[0];

		int logic_count = 0;

		for (int i = 0; i < sequence.length(); i++) {
			if (sequence.charAt(i) == '(') {		
				logic_count ++;
			} else {
				logic_count --;
			}
		}
		
		if (logic_count == 0) {
			System.out.println("Right");
		} else {
			System.out.println("Wrong");
		}
	}
}
