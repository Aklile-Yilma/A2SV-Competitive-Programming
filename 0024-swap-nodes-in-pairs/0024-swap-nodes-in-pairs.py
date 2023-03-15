# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def swapPairs(self, head: Optional[ListNode]) -> Optional[ListNode]:
        
        dummy = ListNode(0, head)
        def swap(head):
            
            if not head or not head.next:
                return head
            
            first = head
            second = head.next
            new_head = second.next
            second.next = first
            
            
            first.next = swap(new_head)
            
            return second
            
        return swap(dummy.next)