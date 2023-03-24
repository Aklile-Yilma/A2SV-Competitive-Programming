# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def deleteDuplicates(self, head: Optional[ListNode]) -> Optional[ListNode]:
        
        #dummy initialize with a first element of 0 and next element of head
        dummy = ListNode(0,next = head)
        
        #a list node slow with the values of dummy
        slow = dummy
        while head:
            
            if head.next and head.val == head.next.val:
                while head.next and head.val == head.next.val:
                    #moving head pointer/ list node
                    head = head.next
                #setting the slow pointer/ list node next (escaping the duplicates)
                slow.next = head.next         
            else:
                # moving the slow pointer
                slow = slow.next
            print(dummy) 
            # resetting head to head.next to iterate over the next head
            head = head.next
            
        return dummy.next

            
        