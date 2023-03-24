# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def pairSum(self, head: Optional[ListNode]) -> int:
        
        #find middle node
        middle_node = self.findMiddleNode(head)
        
        #reverse second half of linked list
        reversed_half = self.reverse(middle_node)
                
        twin_sum = 0
        while reversed_half:
            curr_total = head.val + reversed_half.val
            head = head.next
            reversed_half = reversed_half.next
            twin_sum = max(twin_sum, curr_total)
            
        return twin_sum
        
        
    def findMiddleNode(self, head):
        
        slow = head
        fast = head 
        
        while fast and fast.next:
            slow = slow.next 
            fast = fast.next.next
            
        return slow
    
    def reverse(self, head):
        
        prev = None
        curr = head
        
        while curr:
            temp = curr.next
            curr.next = prev
            prev = curr
            curr = temp
        
        return prev        