class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        
        
        dp = [[0, 0] for _ in range(len(prices))]
        
        #basecase
        dp[-1] = [-prices[-1], prices[-1]]
            
        for idx in range(len(prices)-2, -1, -1):
            
            # buy current or buy next
            buy = max((-prices[idx] + dp[idx+1][1]), dp[idx+1][0])
            
            # sell current or sell next
            sell = max((prices[idx] + max(dp[idx+1][0], 0)), dp[idx+1][1])
            
            dp[idx] = [buy, sell]
            
        return max(dp[0][0], 0)
        
        
# class Solution:
#     def maxProfit(self, prices: List[int]) -> int:     
#         memo = {}
#         # top-down
#         def dfs(idx, canSell):
            
#             if idx >= len(prices):
#                 return 0
            
#             if (idx, canSell) not in memo:
#                 if canSell:
#                     # max of sell or (leave current and sell next)
#                     memo[(idx, canSell)] = max(prices[idx] + dfs(idx+1, False), dfs(idx+1, canSell))
#                 else:
#                     # max of buy or (leave current and buy next)
#                     memo[(idx, canSell)] = max(-prices[idx] + dfs(idx+1, True), dfs(idx+1, canSell))
                
#             return memo[(idx, canSell)]
                        
#         return dfs(0, False)