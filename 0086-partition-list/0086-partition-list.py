# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def partition(self, head: Optional[ListNode], x: int) -> Optional[ListNode]:

        left, right = ListNode(), ListNode()
        left_tail, right_tail = left, right
        curr = head
        
        while curr:
            # set the value of the respective tail
            # move the respective tail
            if curr.val < x:
                left_tail.next = curr
                left_tail = left_tail.next
            else:
                right_tail.next = curr
                right_tail = right_tail.next
            curr = curr.next
            
        # left tail points at right head(.next since it's dummy)
        left_tail.next = right.next
        # right tail points at None since it's now the end node
        right_tail.next = None
        
        # return left.next since it's dummy
        return left.next
            
                
        
        