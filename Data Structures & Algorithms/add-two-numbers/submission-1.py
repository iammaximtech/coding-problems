# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def addTwoNumbers(self, l1: Optional[ListNode], l2: Optional[ListNode]) -> Optional[ListNode]:
        dummy = prev = ListNode()
        carry = 0
        while l1 or l2 or carry>0:
            total = carry
            if l1: 
                total += l1.val
                l1 = l1.next
            if l2: 
                total += l2.val
                l2 = l2.next
            carry, total = total // 10, total %10
            curr = ListNode(total)
            prev.next = curr
            prev = prev.next
        return dummy.next


