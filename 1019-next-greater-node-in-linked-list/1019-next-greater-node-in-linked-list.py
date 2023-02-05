# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def nextLargerNodes(self, head: Optional[ListNode]) -> List[int]:
    
        result = []
		
		# if we don't initialize the stack then we need to check the stack contain value or not  
		#  then we can use old_value, old_index = stack[-1] because there may be possiblity that our stack is empty.
		# so to avoid this if statement in each looping I have use this trick so that my stack is always non empty.
		
        stack = [[float(inf), -1]]
        idx = 0

        while head:

            result.append(0)
            current_value = head.val
            old_value, old_index = stack[-1]

            while stack and old_value < current_value:   # we found next greater element if this condition satisfy

                stack.pop()
                result[old_index] = current_value            # replacing the 0 with the current value bcz it is grater than our old value

                old_value, old_index = stack[-1]


            stack.append([current_value, idx])        # carring index as well as value 
            head = head.next
            idx += 1

        return result

#TLE
# class Solution:
#     def nextLargerNodes(self, head: Optional[ListNode]) -> List[int]:
#         answer = []
#         stack = []
#         slow = head
#         fast = head
        
#         while slow:
#             if slow.val < fast.val:
#                 answer.append(fast.val)
#                 slow = slow.next
                
#         while slow:
#             if slow.val < fast.val:
#                 answer.append(fast.val)
#                 slow=slow.next
#                 fast = slow
#             elif fast.next == None:
#                 # if there are no elements greater than a particular node
#                 answer.append(0)
#                 slow=slow.next
#                 fast = slow
#             else:
#                 fast= fast.next
#         return answer
            
        
        
        