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
        #point tail to head
        curr.next = head
        
        slow = head
        for _ in range(size - k - 1):
            slow = slow.next
        
        #create new head
        head = slow.next
        #create new tail
        slow.next = None
        
        return head