class Solution:
    def __init__(self):
        self.memo = {}
    
    def tribonacci(self, n: int) -> int:
        
        if n == 0:
            return 0
        
        if n == 1 or n == 2:
            return 1
        
        if n not in self.memo:
            self.memo[n] = self.tribonacci(n-3) + self.tribonacci(n-1) + self.tribonacci(n-2)
            
        return self.memo[n]