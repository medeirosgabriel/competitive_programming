# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution(object):
    def reorderList(self, head):
        """
        :type head: Optional[ListNode]
        :rtype: None Do not return anything, modify head in-place instead.
        """
        nodes = []
        node = head
        while (node):
            nodes.append(node)
            node = node.next
        l, r = 0, len(nodes) - 1
        while (l <= r):
            if (l != r):
                aux = nodes[l].next
                nodes[l].next = nodes[r]
                if (aux != nodes[r]): nodes[r].next = aux
                else: nodes[r].next = None
            else:
                nodes[r].next = None
            l += 1
            r -= 1
        return head
