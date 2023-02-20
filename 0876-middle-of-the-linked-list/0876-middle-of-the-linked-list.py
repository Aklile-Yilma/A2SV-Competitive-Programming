# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
# class Solution:
#     def middleNode(self, head: Optional[ListNode]) -> Optional[ListNode]:
        
#         slow = head
#         fast = head
        
#         while fast and fast.next:
#             slow = slow.next
#             fast = fast.next.next
            
#         return slow
    

class Solution:
    def middleNode(self, head: Optional[ListNode]) -> Optional[ListNode]:
        
        
        size = 0
        curr = head
        while curr:
            curr = curr.next
            size += 1    
        middle = math.ceil(size // 2)
        
        slow = head
        curr_idx = 0
        
        while curr_idx < middle:
            slow = slow.next
            curr_idx += 1
        return slow
        
            