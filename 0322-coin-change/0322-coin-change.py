class Solution:        
    def coinChange(self, coins: List[int], amount: int) -> int:
        
        dp = [float('inf')] * (amount + 1)
        #we can reach 0 in 0 ways
        dp[0] = 0
        
        for amt in range(1,amount+1):
            for i in range(len(coins)):
                if amt - coins[i] >= 0:
                    dp[amt] = min( dp[amt], dp[amt-coins[i]] + 1)
                
        return dp[amount] if dp[amount] != float('inf') else -1
    
    