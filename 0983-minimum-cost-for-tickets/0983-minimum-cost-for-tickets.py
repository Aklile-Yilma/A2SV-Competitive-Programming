# class Solution:
#     def __init__(self):
#         self.memo = {}
        
#     def mincostTickets(self, days: List[int], costs: List[int]) -> int:
        
        
#         def dfs(curr_idx):
            
#             if curr_idx == len(days):
#                 return 0
            
#             if curr_idx not in self.memo:
#                 self.memo[curr_idx] = float('inf')
                
#                 for d, c in zip([1, 7, 30], costs):
#                     #find next index
#                     j = curr_idx
#                     while j < len(days) and days[j] < days[curr_idx] + d:
#                         j += 1
                        
#                     self.memo[curr_idx] = min(self.memo[curr_idx], c + dfs(j))
                
#             return self.memo[curr_idx]
        
#         return dfs(0)
    
    
class Solution:
    def mincostTickets(self, days: List[int], costs: List[int]) -> int:
        
        max_day = days[-1]
        days_set = set(days)
        
        dp = [float('inf')] * (max_day + 1)
        dp[0] = 0
        
        for d in range(1, max_day + 1):
            dp[d] = dp[d-1]
            if d in days_set:
                dp[d] = min(dp[d-1] + costs[0], dp[max(0, d-7)] + costs[1], dp[max(0, d-30)] + costs[2])
                
        return dp[-1]