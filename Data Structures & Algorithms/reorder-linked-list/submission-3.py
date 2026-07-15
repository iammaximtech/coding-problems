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
        last = mid.next = None
        while slow:
           curr = slow
           currnext = slow.next
           curr.next =last
           last = curr
           slow = currnext
        tail = last
        

        while head and tail:
            hnext = head.next
            tnext = tail.next
            head.next = tail
            tail.next = hnext
            head = hnext
            tail = tnext
        
        
            
            
