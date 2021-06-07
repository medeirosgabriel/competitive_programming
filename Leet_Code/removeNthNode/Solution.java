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

import java.util.List;
import java.util.ArrayList;

class Solution {

	public static ListNode removeNthFromEnd(ListNode node, int n) {
		
		List<ListNode> list = new ArrayList<>();
		ListNode aux = node;

		while (aux != null) {
			list.add(aux);
			aux = aux.next;
		}

		int size = list.size();
		aux = list.get(size - n);
		list.get(size - n - 1).next = aux.next;
		
		return list.get(0);
	}
}
