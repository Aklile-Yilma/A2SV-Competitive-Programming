class StockSpanner:

    def __init__(self):
        #decreasing monostack
        self.stack = []
        
    def next(self, price: int) -> int:
        span = 1
        
        while self.stack and self.stack[-1][0] <= price:
            curr_price, curr_span = self.stack.pop()
            span += curr_span
        
        self.stack.append([price, span])
        
        return span
            


# Your StockSpanner object will be instantiated and called as such:
# obj = StockSpanner()
# param_1 = obj.next(price)