class Solution:
    def maxProfit(self, prices: List[int]) -> int:
           
        left = 0
        max_profit = 0
        
        for right in range(1, len(prices)):
            
            if prices[left] < prices[right]:
                max_profit = max(max_profit, prices[right] - prices[left])
            else:
                left = right
                
        return max_profit
                