# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def mergeTwoLists(self, list1: Optional[ListNode], list2: Optional[ListNode]) -> Optional[ListNode]:
        
        def merge(merged_list, list1, list2):
            
            if not list1 or not list2:
                if list1:
                    merged_list.next = list1
                    return 
                elif list2:
                    merged_list.next = list2
                    return 
                return None
            
            if list1.val <= list2.val:
                merged_list.next = ListNode(list1.val)
                merge(merged_list.next, list1.next, list2)
            else:
                merged_list.next = ListNode(list2.val)
                merge(merged_list.next, list1, list2.next)
            
        dummy = ListNode()
        dummy_head = dummy
        merge(dummy, list1, list2)
        
        return dummy_head.next
            
            
        
#         list3 = ListNode()
#         list3_head = list3
        
#         while list1 and list2:
            
#             if list1.val <= list2.val:
#                 list3.next = list1
#                 list1 = list1.next
#             else:
#                 list3.next = list2
#                 list2 = list2.next
                
#             list3 = list3.next
            
#         if list1:
#             list3.next = list1
        
#         if list2:
#             list3.next = list2
            
#         return list3_head.next
            
        