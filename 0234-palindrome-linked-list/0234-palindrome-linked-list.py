# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def isPalindrome(self, head: Optional[ListNode]) -> bool:
        
        # find the middle node
        middle = self.middleNode(head)
        
        # reverse the linked list after the middle node
        tail = self.reverseList(middle)
        
        # check the first half and reversed last half are equal
        
        left, right = head, tail
        
        while right:
            if right.val != left.val:
                return False
            left = left.next
            right = right.next
            
        return True
        
    def middleNode(self, head: Optional[ListNode]) -> ListNode:
        slow = head
        fast = head
        
        #find the middle of the linked list
        while fast and fast.next:
            slow = slow.next
            fast = fast.next.next
            
        return slow
        
    def reverseList(self, head: Optional[ListNode]) -> ListNode:
        
        prev = None
        curr = head
        
        while curr:
            temp = curr.next
            curr.next = prev
            prev = curr
            curr = temp
            
        return prev
        