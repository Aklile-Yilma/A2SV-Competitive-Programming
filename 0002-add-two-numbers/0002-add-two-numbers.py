# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def addTwoNumbers(self, l1: Optional[ListNode], l2: Optional[ListNode]) -> Optional[ListNode]:
        
        dummy = ListNode()
        cur = dummy
        carry = 0
        while l1 or l2 or carry:
            
            v1 = l1.val if l1 else 0
            v2 = l2.val if l2 else 0
            
            #new digit
            val = v1 + v2 + carry
            #remove new carry
            carry = val // 10
            val =  val % 10
            
            #link new digit
            cur.next  = ListNode(val)
            
            #update pointers
            cur = cur.next
            l1 = l1.next if l1 else None
            l2 = l2.next if l2 else None
            
        return dummy.next

#Brute force approach
# class Solution:
#     def addTwoNumbers(self, l1: Optional[ListNode], l2: Optional[ListNode]) -> Optional[ListNode]:
        
#         l1_reverse = self.reverseList(l1)
#         l2_reverse = self.reverseList(l2)
                
#         l1_num = self.getNumber(l1_reverse)
#         l2_num = self.getNumber(l2_reverse)
#         l3_num = str(l1_num + l2_num)
        
#         l3 = ListNode()
#         curr = l3
        
#         print(curr)
#         for num in l3_num:
#             curr.next = ListNode(num)
#             curr = curr.next
#         #remove dummy node
#         l3 = l3.next
        
#         l3_reverse = self.reverseList(l3)
        
#         return l3_reverse
        
#     def reverseList(self, head: Optional[ListNode]) -> Optional[ListNode]:

#         prev = None
#         curr = head
        
#         while curr:
#             temp = curr.next
#             curr.next = prev
#             prev = curr
#             curr = temp
            
#         # return the head: prev is the new head
#         return prev
    
    
#     def getNumber(self, head: Optional[ListNode]) -> int:
        
#         curr = head
#         nums = []
        
#         while curr:
#             nums.append(str(curr.val))
#             curr = curr.next
        
#         return int(''.join(nums))
            
    
        