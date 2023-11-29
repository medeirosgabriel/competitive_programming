# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution(object):
    def mergeKLists(self, lists):
        """
        :type lists: List[ListNode]
        :rtype: ListNode
        """
        n = 0
        dic = {}
        for i in range(len(lists)):
            if (lists[i] != None and lists[i].val != None):
                dic[i] = lists[i]
                n += 1

        head, tail = None, None
        while (n != 0):
            chosen, smaller = -1, float('inf')
            for k in dic.keys():
                if (dic[k] != None and dic[k].val < smaller):
                    chosen, smaller = k, dic[k].val

            if (head == None):
                head = ListNode()
                head.val = dic[chosen].val
                tail = head
            else:
                tail.next = ListNode()
                tail = tail.next
                tail.val = dic[chosen].val 
                
            dic[chosen] = dic[chosen].next
            if (dic[chosen] == None): n -= 1

        return head
