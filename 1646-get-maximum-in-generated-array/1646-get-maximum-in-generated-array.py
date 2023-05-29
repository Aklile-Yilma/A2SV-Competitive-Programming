class Solution:
    def __init__(self):
        self.memo = {}
        self.max = float('-inf')        
    def getMaximumGenerated(self, n: int) -> int:
        
        def recursion(n):
            if n <= 1:
                return n

            if n not in self.memo:
                if n % 2 == 0:
                     self.memo[n] = recursion(n // 2)

                if n % 2 != 0:
                    self.memo[n] = recursion(n // 2) + recursion(n // 2 + 1)
                
            return self.memo[n]
        
        for i in range(n+1):
            if i not in self.memo:
                res = recursion(i)
                self.max = max(self.max, res)
                
        return self.max