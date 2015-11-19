# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution(object):
    def reverseList(self, head):
        """
        :type head: ListNode
        :rtype: ListNode
        """
        dummy = head
        tmp = dummy
        
        while head and head.next != None:
            dummy = head.next
            head.next = dummy.next
            dummy.next = tmp
            tmp = dummy
        return dummy