# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def removeNthFromEnd(self, head: Optional[ListNode], n: int) -> Optional[ListNode]:
        
        
        size = 0
        curr = head
        
        while curr:
            size += 1
            curr = curr.next
            
        
        if size - n == 0:
            head = head.next
            return head
            
        curr = head
        idx = 1
        while curr:
            if size - n == idx:
                curr.next = curr.next.next
                
            idx += 1
            curr = curr.next
            
        return head
            
                