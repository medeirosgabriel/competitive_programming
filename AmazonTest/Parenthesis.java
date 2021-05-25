public class Parenthesis {

	public static void main(String[] args) {

		String sequence = args[0];

		int logic_count = 0;

		for (int i = 0; i < sequence.length(); i++) {
			logic_count += (sequence.charAt(i) == '(') ? 1 : -1;
		}
		
		String result = (logic_count == 0) ? "Right" : "Wrong";

		System.out.println(result);
	}
}
