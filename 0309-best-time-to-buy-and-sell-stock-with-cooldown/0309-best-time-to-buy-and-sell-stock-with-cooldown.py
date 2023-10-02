class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        
        memo = {}
        def dfs(idx, canSell):
            
            if idx >= len(prices):
                return 0
            
            if (idx, canSell) not in memo:
                if canSell:
                    # max of sell or (leave current and sell next)
                    memo[(idx, canSell)] = max(prices[idx] + dfs(idx+2, False), dfs(idx+1, canSell))
                else:
                    # max of buy or (leave current and buy next)
                    memo[(idx, canSell)] = max(-prices[idx] + dfs(idx+1, True), dfs(idx+1, canSell))
                    
            return memo[(idx, canSell)]
        
        return dfs(0, False)