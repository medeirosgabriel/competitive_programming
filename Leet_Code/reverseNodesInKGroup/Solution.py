# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution(object):
    def reverse(self, node, sub, l, curr, k):
        if (node != None):
            l.append(node.val)
            curr += 1
            if (curr == k):
                for _ in range(len(l)):
                    sub.val = l.pop()
                    sub = sub.next
                self.reverse(node.next, node.next, [], 0, k)
            else:
                self.reverse(node.next, sub, l, curr, k)

    def reverseKGroup(self, head, k):
        """
        :type head: ListNode
        :type k: int
        :rtype: ListNode
        """
        if (k > 0):
            self.reverse(head, head, [], 0, k)
        return head
