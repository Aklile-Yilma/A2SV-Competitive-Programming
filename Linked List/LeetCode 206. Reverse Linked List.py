# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def reverseList(self, head: Optional[ListNode]) -> Optional[ListNode]:

        prev = None
        curr = head

        while curr:

            tmp = curr.next
            curr.next = prev
            prev = curr
            curr = tmp

        return prev



# Recursive

# class Solution:
#     def reverseList(self, head: Optional[ListNode]) -> Optional[ListNode]:

#         def helper(prev, curr):

#             if not curr:
#                 return prev

#             #recursive call
#             tail = helper(curr, curr.next)
#             curr.next = prev

#             return tail

#         return helper(None, head)
