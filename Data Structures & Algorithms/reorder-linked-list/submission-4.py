# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def reorderList(self, head: Optional[ListNode]) -> None:
        if not head:
            return

        slow, fast = head, head.next
        while fast and fast.next:
            slow = slow.next
            fast = fast.next.next
        
        mid = slow
        slow = slow.next
        prev = mid.next = None
        while slow:
           curr = slow
           currnext = slow.next
           curr.next =prev
           prev = curr
           slow = currnext
        tail = prev
        

        while head and tail:
            hnext = head.next
            tnext = tail.next
            head.next = tail
            tail.next = hnext
            head = hnext
            tail = tnext
        
        
            
            
