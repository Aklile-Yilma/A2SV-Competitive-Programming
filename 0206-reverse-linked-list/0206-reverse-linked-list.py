# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
# class Solution:
#     def reverseList(self, head: Optional[ListNode]) -> Optional[ListNode]:

#         prev = None
#         curr = head
        
#         while curr:
#             temp = curr.next
#             curr.next = prev
#             prev = curr
#             curr = temp
            
#         # return the head: prev is the new head
#         return prev
    
    
    
# Recursive

class Solution:
    def reverseList(self, head: Optional[ListNode]) -> Optional[ListNode]:
        
        def helper(prev, curr):
            # if reached null
            if not curr:
                return prev
            
            new_head = curr.next
            curr.next = prev
            #recursive call
            return helper(curr, new_head)
                    
        return helper(None, head)
    
    
