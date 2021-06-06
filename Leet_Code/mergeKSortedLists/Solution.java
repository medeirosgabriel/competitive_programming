/**
 * Definition for singly-linked list.
 * public class ListNode {
 *     int val;
 *     ListNode next;
 *     ListNode() {}
 *     ListNode(int val) { this.val = val; }
 *     ListNode(int val, ListNode next) { this.val = val; this.next = next; }
 * }
 */

class Solution {
	
	public static ListNode mergeKLists(ListNode[] lists) {
        
		int size = lists.length;
		ListNode r = new ListNode();
		ListNode head = r;

		while (size != 0) {
			int index = -1;
			int v = 100000;
			for (int j = 0; j < lists.length; j++) {
				if (lists[j] != null && lists[j].val < v) {
					v = lists[j].val;
					index = j;
				}
			}

			r.val = v;
			r.next = new ListNode();
			r = r.next;
			if (lists[index].next == null) { size --; }
			lists[index] = lists[index].next;
		}

		return head;
	
	}
}
