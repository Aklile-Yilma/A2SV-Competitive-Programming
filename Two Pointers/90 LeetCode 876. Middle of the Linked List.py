 # Definition for singly-linked list.

class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next


class Solution:
    def middleNode(self, head: Optional[ListNode]) -> Optional[ListNode]:
        slow_pointer = head #this will go forward 1 at a time
        fast_pointer = head #move forward 2 at a time

        while fast_pointer and fast_pointer.next: #while our fast node exists and isn't the last node
            slow_pointer = slow_pointer.next  #slow pointer moves forward just 1 spot
            fast_pointer = fast_pointer.next.next #fast pointer moves forward by two

        return slow_pointer #By the time the fast pointer makes it to the end of the list, slow will be right in the middle since the fast pointer goes through the list twice as quickly as the slow pointer.



