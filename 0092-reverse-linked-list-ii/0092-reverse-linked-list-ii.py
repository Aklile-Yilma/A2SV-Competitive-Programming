# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def reverseBetween(self, head: Optional[ListNode], left: int, right: int) -> Optional[ListNode]:
        
        
        prefix = ListNode()
        window = ListNode()
        postfix = ListNode()
        
        curr = head
        prefix_tail = prefix
        window_tail = window
        postfix_tail = postfix
        idx = 0
        
        while curr:
            idx += 1
            if idx < left:
                prefix_tail.next = curr
                prefix_tail =  prefix_tail.next
            elif left <= idx <= right:
                window_tail.next = curr
                window_tail = window_tail.next
            else:
                postfix_tail.next = curr
                postfix_tail = postfix_tail.next
                
            curr = curr.next
            
        # send only the window without postfix
        window_tail.next = None
        # reverse window skipping dummy node
        window = self.reverseList(window.next)
        # connect prefix to window
        prefix_tail.next = window
        # connect window to postfix(skipping dummy node)        
        # since the tail of the window is reversed find new tail
        curr = window
        while curr.next:
            curr = curr.next
        # skip dummy node
        curr.next = postfix.next
        
        return prefix.next

        
    def reverseList(self, head: Optional[ListNode]) -> Optional[ListNode]:

        prev = None
        curr = head
        
        while curr:
            temp = curr.next
            curr.next = prev
            prev = curr
            curr = temp
            
        # return the head: prev is the new head
        return prev
    