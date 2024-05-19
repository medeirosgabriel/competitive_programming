# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution(object):

    def removeNthFromEnd(self, head, n):
        l = []
        count = 0
        node = head
        while (node != None):
            l.append(node)
            count += 1
            node = node.next
        if (n == count and count > 1):
            return l[1]
        if (n + 1 > count):
            return None
        else:
            l[-(n + 1)].next = l[-n].next
        return head
