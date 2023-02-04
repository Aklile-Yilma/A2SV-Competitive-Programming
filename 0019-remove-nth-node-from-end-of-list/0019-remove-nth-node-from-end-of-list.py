# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def removeNthFromEnd(self, head: Optional[ListNode], n: int) -> Optional[ListNode]:
        
        dummy = ListNode(0, head)
        slow = dummy
        fast = head
        
        # slow and fast pointer have a fixed window size of (N) PLUS ONE because of dummy node
        while n>0 and fast:
            fast = fast.next
            n-=1
            
        while fast:
            slow = slow.next
            fast = fast.next
        #delete the node
        slow.next = slow.next.next
            
        return dummy.next
        

# class Solution:
#     def removeNthFromEnd(self, head: Optional[ListNode], n: int) -> Optional[ListNode]:
        
        
#         size = 0
#         curr = head
#         # find size of linked list
#         while curr:
#             size += 1
#             curr = curr.next
            
#         # edge case: remove the first node
#         if size - n == 0:
#             head = head.next
#             return head
            
#         curr = head
#         idx = 1
#         while curr:
#             # skip nth node from end of list
#             if size - n == idx:
#                 curr.next = curr.next.next
#             idx += 1
#             curr = curr.next
            
#         return head
            
                