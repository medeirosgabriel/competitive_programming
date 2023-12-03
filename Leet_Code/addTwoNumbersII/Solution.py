# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution(object):

    def addTwoNumbers(self, l1, l2):
        """
        :type l1: ListNode
        :type l2: ListNode
        :rtype: ListNode
        """
        head, tail, dec = None, None, 0
        while (l1 != None and l2 != None):
            n1, n2 = l1.val, l2.val
            s = n1 + n2 + dec
            dec = 0
            if (tail == None):
                tail = ListNode()
                head = tail
            else:
                tail.next = ListNode()
                tail = tail.next
            tail.val = s % 10
            dec = int(s/10)
            l1, l2 = l1.next, l2.next

        for l in [l1, l2]:
            while (l != None ):
                n = l.val
                s = n + dec
                dec = 0
                if (tail == None):
                    tail = ListNode()
                    head = tail
                else:
                    tail.next = ListNode()
                    tail = tail.next
                tail.val = s % 10
                dec = int(s/10)
                l = l.next
        
        if (dec != 0):
            tail.next = ListNode()
            tail = tail.next
            tail.val = dec

        return head
        
