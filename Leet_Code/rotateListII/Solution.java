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
    public ListNode rotateRight(ListNode head, int k) {
        if (head == null || k == 0) return head;
        ListNode node = head, tail = null;
        int n = 0;
        while (node != null) {
            if (node.next == null) {
                tail = node;
            }
            node = node.next;
            n ++;
        }

        int diff = k % n;
        int pos = n + diff - 1;
        int newTailPos = n - diff;
        ListNode newTail = head;

        while (newTail != null && newTailPos > 1) {
            newTail = newTail.next;
            newTailPos--;
        }

        tail.next = head;
        head = newTail.next;
        newTail.next = null;

        return head;
    }
}
