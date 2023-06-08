# class Solution:
#     def minCostClimbingStairs(self, cost: List[int]) -> int:
        
#         self.memo = {}
#         def recursion(idx):
#             nonlocal cost
#             if idx == len(cost)-1 or idx == len(cost)-2:
#                 return cost[idx]
            
#             if idx not in self.memo:
#                 self.memo[idx] = [recursion(idx+1), recursion(idx+2)]
                
#             return cost[idx] + min(self.memo[idx])
            
#         return min(recursion(0), recursion(1))
    
    
class Solution:
    def minCostClimbingStairs(self, cost: List[int]) -> int:
        
        size = len(cost) + 1
        dp = [float('inf')] * size
        dp[0] = cost[0]
        dp[1] = cost[1]
        cost.append(0)
        
        for i in range(2, size):
            dp[i] = min(dp[i-1], dp[i-2]) + cost[i]
            
        return dp[size-1]