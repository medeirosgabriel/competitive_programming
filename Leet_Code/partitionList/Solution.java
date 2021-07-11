class Solution {
	
	public static ListNode partition(ListNode head, int x) {
		ListNode[] list = new ListNode[4];
		
		partition(head, list, x);
		
		if (list[1] != null) {
			list[1].next = list[2];
		} else {
			list[0].next = null;
		}

		if (list[3] != null) {
			list[3].next = null;
		} else {
			list[2].next = null;
		}

		return (list[0] == null) ? list[2] : list[0];
	}

	private static void partition(ListNode node, ListNode[] list, int x) {
		
		if (node.val < x) {
			if (list[0] == null) {
				list[0] = node;
				list[1] = node;
			} else {
				list[1].next = node;
				list[1] = node;
			}
		} else {
			if (list[2] == null) {
				list[2] = node;
				list[3] = node;
			} else {
				list[3].next = node;
				list[3] = node;
			}
		}
		
		if (node.next != null) {
			partition(node.next, list, x);
		}
	}
}

