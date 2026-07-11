# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution:
    def hasCycle(self, head: Optional[ListNode]) -> bool:
        if not head:
            return False
        if not head.next:
            return False
        if head.next == head:
            return True
        slow = head
        fast = head.next
        while slow and fast:
            if slow.val == fast.val and slow.next == fast.next:
                return True
            if slow.next and fast.next:
                slow = slow.next
                fast = fast.next.next
            else:
                return False
        return False
        