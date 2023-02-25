class Solution:
    def timeRequiredToBuy(self, tickets: List[int], k: int) -> int:
        
        time = 0
        
        while tickets[k] != 0:
            
            if tickets[0] != 0:
                tickets[0] -= 1
                time += 1
            
            front = tickets.pop(0)
            tickets.append(front)
            
            if k > 0:
                k -= 1
            else:
                k = len(tickets) - 1
            
        return time
       

# class Solution:
#     def timeRequiredToBuy(self, tickets: List[int], k: int) -> int:
        
#         time = 0
        
#         while tickets[k] != 0:
            
#             for idx in range(len(tickets)):
#                 if tickets[idx] != 0:
#                     tickets[idx] -= 1
#                     time += 1
                
#                 if tickets[k] == 0:
#                     break
                
#         return time