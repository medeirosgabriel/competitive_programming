public class Test {

	public static void main(String[] args) {

		ListNode n9 = new ListNode(22, null);
		ListNode n8 = new ListNode(16, n9);
		ListNode n7 = new ListNode(14, n8);
		ListNode n6 = new ListNode(48, null);
		ListNode n5 = new ListNode(12, n6);
		ListNode n4 = new ListNode(5, n5);
		ListNode n3 = new ListNode(1, n4);
		ListNode n2 = new ListNode(22, null);
		ListNode n1 = new ListNode(15, n2);
		ListNode n0 = new ListNode(1, n1);
		
		ListNode r = Solution.mergeKLists(new ListNode[]{n0, n3, n7});

		while (r != null) {

			System.out.println(r.val + " ");
			r = r.next;
		}
	}
}
