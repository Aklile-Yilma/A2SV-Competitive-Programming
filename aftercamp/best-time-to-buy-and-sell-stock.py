class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        
        curr_min = float('inf')
        dp = [0] * len(prices)
        
        for idx, price in enumerate(prices):
            # keep track of the min value upto current
            curr_min = min(curr_min, price)
            # each dp will be the profit between the prev price
            dp[idx] = price - curr_min
          
        return max(dp)