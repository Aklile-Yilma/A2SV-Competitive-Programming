# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def rotateRight(self, head: Optional[ListNode], k: int) -> Optional[ListNode]:

        if not head:
            return None
        
        size = 1
        curr = head
        while curr.next:
            curr = curr.next
            size += 1
            
        k = k % size
        curr.next = head
        
        slow = head
        slow_head = slow
        for _ in range(size - k - 1):
            slow = slow.next
        
        head = slow.next
        slow.next = None
        
        return head