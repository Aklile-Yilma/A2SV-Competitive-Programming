class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        
        prices.append(float('-inf'))
        total = 0
        buy_index = 0
        
        for sell_index in range(len(prices)-1):
            
            if prices[sell_index] > prices[sell_index+1]:
                total += prices[sell_index] - prices[buy_index]
                buy_index = sell_index + 1
                
        return total
                
    
