# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution(object):
    
    def swap(self, last, actual, control):
        if (last == None):
            if (actual != None):
                self.swap(actual, actual.next, not(control))
        elif(actual == None):
            return
        else:
            if (control):
                temp = actual.val
                actual.val = last.val
                last.val = temp
            if (actual.next != None): 
                self.swap(actual, actual.next, not(control))
            else:
                return


    def swapPairs(self, head):
        self.swap(None, head, False)
        return head
