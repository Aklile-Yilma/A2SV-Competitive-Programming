# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def mergeKLists(self, lists: List[Optional[ListNode]]) -> Optional[ListNode]:
        
        heap = []
        
        for l in lists:
            curr = l
            while curr:
                heappush(heap, curr.val)
                curr = curr.next
                
        dummy = ListNode(-1)
        curr = dummy
        
        while heap:
            newNode = ListNode(heappop(heap))
            curr.next = newNode
            curr = curr.next
            
        return dummy.next
        