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
        while slow and fast:
            slow = slow.next
            if fast.next and fast.next.next:
                fast = fast.next.next
            else:
                break
        
        mid = slow
        slow = slow.next if slow else None
        last = mid.next = None
        while slow:
           curr = slow
           next = slow.next
           curr.next =last
           last = curr
           slow = next
        tail = last
        

        while head and tail:
            hnext = head.next
            tnext = tail.next
            head.next = tail
            tail.next = hnext
            head = hnext
            tail = tnext
        
        
            
            
