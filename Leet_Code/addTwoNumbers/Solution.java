import java.util.List;
import java.util.ArrayList;

public class Solution {

	public static ListNode addTwoNumbers(ListNode l1, ListNode l2) {
		
		List<Integer> ls1 = addTwoNumbers(l1);
		List<Integer> ls2 = addTwoNumbers(l2);
		
		ListNode r = new ListNode();
		ListNode aux = r;

		int i = 0, carry_out = 0;

		while (i < ls1.size() && i < ls2.size()) {
			
			aux.val = (ls1.get(i) + ls2.get(i) + carry_out)%10;
			carry_out = (ls1.get(i) + ls2.get(i) + carry_out)/10;

			aux.next = new ListNode();
			aux = aux.next;

			i++;
		}

		while (i < ls1.size()) {

                        aux.val = (ls1.get(i) + carry_out)%10;
                        carry_out = (ls1.get(i) + carry_out)/10;

                        aux.next = new ListNode();
                        aux = aux.next;

			i++;
                }

		while (i < ls2.size()) {

                        aux.val = (ls2.get(i) + carry_out)%10;
                        carry_out = (ls2.get(i) + carry_out)/10;

                        aux.next = new ListNode();
                        aux = aux.next;

			i++;
                }

		
		return r;
	}

	private static List<Integer> addTwoNumbers(ListNode l) {

		if (l.next == null) {

			List<Integer> list = new ArrayList<>();
			list.add(l.val);	
			return list;

		} else {

			List<Integer> list = addTwoNumbers(l.next);
			list.add(l.val);
			return list;

		}

	}
}
