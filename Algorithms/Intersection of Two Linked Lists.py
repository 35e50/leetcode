# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution:
    # @param two ListNodes
    # @return the intersected ListNode
    def getIntersectionNode(self, headA, headB):
        lenA = 0; lenB = 0
        tmpA = ListNode(0); tmpA.next = headA
        tmpB = ListNode(0); tmpB.next = headB
        while tmpA.next != None:
            lenA += 1
            tmpA = tmpA.next
        while tmpB.next != None:
            lenB += 1
            tmpB = tmpB.next
        if tmpA != tmpB: return None
        if lenA < lenB:
            headA, headB = headB, headA
        diff = abs(lenA - lenB)
        for i in xrange(diff):
            headA = headA.next
        while headA != headB:
            headA = headA.next
            headB = headB.next
        return headA