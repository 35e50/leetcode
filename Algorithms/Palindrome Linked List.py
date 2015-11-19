# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution(object):
    def isPalindrome(self, head):
        """
        :type head: ListNode
        :rtype: bool
        """
        tmp = head
        list = []
        while tmp != None:
            list.append(tmp.val)
            tmp = tmp.next
        for i in range(len(list)/2):
            if list[i] != list[len(list)-1-i]:
                return False
        return True