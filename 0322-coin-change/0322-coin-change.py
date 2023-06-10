# class Solution:        
#     def coinChange(self, coins: List[int], amount: int) -> int:
        
#         dp = [float('inf')] * (amount + 1)
#         #we can reach 0 in 0 ways
#         dp[0] = 0
        
#         for amt in range(1,amount+1):
#             for i in range(len(coins)):
#                 if amt - coins[i] >= 0:
#                     dp[amt] = min( dp[amt], dp[amt-coins[i]] + 1)
                
#         return dp[amount] if dp[amount] != float('inf') else -1
    
    
class Solution:      
    def coinChange(self, coins: List[int], amount: int) -> int:
        
        def dp(remaining, memo):
            
            nonlocal min_coins
            #basecase 
            if remaining < 0:
                return float('inf')
            
            if remaining == 0:  
                return 0
            
            if remaining in memo:
                return memo[remaining]
            

            memo[remaining] = min(dp(remaining - coin, memo) + 1 for coin in coins)  
                        
            return memo[remaining]
                    
        min_coins = dp(amount, {})
                    
        return min_coins if min_coins != float('inf') else -1