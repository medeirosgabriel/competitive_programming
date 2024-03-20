# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution(object):
    def hasCycle(self, head):
        """
        :type head: ListNode
        :rtype: bool
        """
        MAX = 200000
        node = head
        while (node != None):
            if (node.val == MAX):
                return True
            else:
                node.val = MAX
            node = node.next
        return False
