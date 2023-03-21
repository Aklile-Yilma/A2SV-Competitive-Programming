# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def sortList(self, head: Optional[ListNode]) -> Optional[ListNode]:
        if head and head.next:
            
            left = head
            right = self.divide(head)        
            left_ = self.sortList(left)
            right_ = self.sortList(right)
        
            return self.merge(left_, right_)
        
        return head
        
    def divide(self, head):
        if head.next == None:
            return head
        
        slow = ListNode(0, head)
        fast = head
        
        while fast and fast.next:
            slow = slow.next
            fast = fast.next.next
            
        middle = slow.next
        slow.next = None
        
        return middle
        
        
    def merge(self, l1, l2):
        if not l1 or not l2:
            return l1 or l2
        if l1.val < l2.val:
            l1.next = self.merge(l1.next, l2)
            return l1
        else:
            l2.next = self.merge(l1, l2.next)
            return l2


            