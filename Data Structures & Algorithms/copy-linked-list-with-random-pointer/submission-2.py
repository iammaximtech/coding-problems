"""
# Definition for a Node.
class Node:
    def __init__(self, x: int, next: 'Node' = None, random: 'Node' = None):
        self.val = int(x)
        self.next = next
        self.random = random
"""

class Solution:
    def copyRandomList(self, head: 'Optional[Node]') -> 'Optional[Node]':
        if not head: return None
        
        curr = head
        while curr:
            copy = Node(curr.val)
            copy.next = curr.next
            curr.next = copy
            curr = copy.next
        
        curr = head
        while curr:
            copy = curr.next
            if curr.random:
                copy.random = curr.random.next
            curr = curr.next.next
        
        curr = head
        copy = curr.next
        dummy = Node(0)
        dummy.next = copy
        while copy.next:
            curr.next = copy.next
            curr = curr.next
            copy.next = curr.next
            copy = copy.next
        curr.next = None
        return dummy.next


        