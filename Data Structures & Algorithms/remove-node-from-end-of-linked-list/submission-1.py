# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def removeNthFromEnd(self, head: Optional[ListNode], n: int) -> Optional[ListNode]:
        if not head: return head
        length = 0
        curr = head
        while curr:
            length += 1
            curr = curr.next
        target = length - n +1

        i = 0
        dummy = prev = ListNode(0,head)
        while head:
            i+=1
            if i == target:
                prev.next = head.next
            else:
                prev = prev.next
            head = head.next
        return dummy.next
                