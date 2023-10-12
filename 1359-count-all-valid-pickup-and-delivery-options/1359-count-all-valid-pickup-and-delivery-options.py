class Solution:
    def countOrders(self, n: int) -> int:
        
        if n == 1:
            return 1
        
        return (n * (self.countOrders(n-1) * (2*n - 1))) %  (10**9 + 7)