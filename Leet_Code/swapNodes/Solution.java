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

	public static ListNode swapPairs(ListNode head) {
        	
		if (head.next != null) {
		
			swapPairs(head, head.val, -1);

		}

		return head;
	}

	private static int swapPairs(ListNode node, int value, int flag) {

		if (node.next == null) {

			if (flag == 1) {
				
				int v = node.val;
                        	node.val = value;
				return v;

			}

			return -1;
			
		} else {
			
			int v = swapPairs(node.next, node.val, -flag);

			if (flag == 1) {
				
				v = node.val;
				node.val = value;
				return v;

			} else {

				node.val = v;
				return -1;
			}

		}

	}
}
