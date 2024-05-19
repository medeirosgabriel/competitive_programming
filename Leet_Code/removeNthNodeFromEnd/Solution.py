# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution(object):

    def recursion(self, node, n):
            if (node != None):
                control = self.recursion(node.next, n)
                if (control == 0):
                    next_ = node.next
                    if (next_ == None):
                        node.next = next_
                    else:
                        node.next = next_.next
                return control - 1
            return n

    def removeNthFromEnd(self, head, n):
        """
        :type head: ListNode
        :type n: int
        :rtype: ListNode
        """
        nn = self.recursion(head, n)
        if (nn == 0):
            head = head.next
        return head
