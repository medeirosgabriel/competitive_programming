public class Test {

	public static void main(String[] args) {

		ListNode n9 = new ListNode();
		ListNode n8 = new ListNode();
		ListNode n7 = new ListNode();
		ListNode n6 = new ListNode(3, null);
		ListNode n5 = new ListNode(4, n6);
		ListNode n4 = new ListNode(5, n5);
		ListNode n3 = new ListNode(7, n4);
		ListNode n2 = new ListNode(3, n3);
		ListNode n1 = new ListNode(2, n2);
		ListNode n0 = new ListNode(1, n1);
		
		ListNode r = Solution.partition(n0, 4);

		while (r != null) {
			System.out.println(r.val);
			r = r.next;
		}
	}
}
