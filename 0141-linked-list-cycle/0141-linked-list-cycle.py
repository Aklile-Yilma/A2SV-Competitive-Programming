# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution:
    def hasCycle(self, head: Optional[ListNode]) -> bool:
        
        last_seen = {}
        
        pos = 0
        curr = head
        print(curr)
        
        while curr:
            if curr in last_seen:
                return True
            
            last_seen[curr] = pos
            pos += 1
            curr = curr.next
            
        return False
    

        node_set = set()
        while(head):
            if head in node_set:
                return True
            node_set.add(head)
            head = head.next
        return False

            
            