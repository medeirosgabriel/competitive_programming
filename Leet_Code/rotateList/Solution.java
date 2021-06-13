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
	
	public static ListNode rotateRight(ListNode head, int k) {
        	
		for (int i = 0; i < k; i++) {
			ListNode newHead = rotateRight(head, null);
			newHead.next = head;
			head = newHead;
		}

		return head;

	}

	private static ListNode rotateRight(ListNode node, ListNode previous) {
		if (node.next != null) {
			return rotateRight(node.next, node);
		} else {
			previous.next = null;
			return node;
		}
		
	}
}

