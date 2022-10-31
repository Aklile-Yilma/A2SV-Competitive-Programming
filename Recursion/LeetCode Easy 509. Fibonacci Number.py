class Solution:
    def fib(self, n: int) -> int:
        
        if(n == 0):
            return 0
        if(n == 1):
            return 1
        
        # for every number find the fibonacci number of its (n-1) and (n-2)
        return self.fib(n-1) + self.fib(n-2)
    
