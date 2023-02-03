# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def deleteDuplicates(self, head: Optional[ListNode]) -> Optional[ListNode]:
        
        curr = head
        prev = None
        
        while curr:
            if prev and curr.val == prev.val:
                prev.next = curr.next
            else:
                #only move prev if it's not non-duplicate
                prev = curr
                
            curr = curr.next
            
        return head
        