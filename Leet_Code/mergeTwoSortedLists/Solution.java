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

    public ListNode mergeTwoLists(ListNode list1, ListNode list2) {

        ListNode out = null;

        if (list1 != null || list2 != null) {
            out = new ListNode();
            ListNode last = null;
            ListNode curr = out;

            while (list1 != null && list2 != null) {
                if (list1.val <= list2.val) {
                    curr.val = list1.val;
                    list1 = list1.next;
                } else {
                    curr.val = list2.val;
                    list2 = list2.next;
                }
                last = curr;
                curr.next = new ListNode();
                curr = curr.next;
            }

            while (list1 != null) {
                curr.val = list1.val;
                list1 = list1.next;
                last = curr;
                curr.next = new ListNode();
                curr = curr.next;
            }

            while (list2 != null) {
                curr.val = list2.val;
                list2 = list2.next;
                last = curr;
                curr.next = new ListNode();
                curr = curr.next;
            }

            if (last != null) {
                last.next = null;
            }
        }
        return out;
    }
}
