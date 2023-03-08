class Solution:
    def kthGrammar(self, n: int, k: int) -> int:
        
        if n == 1:
            return 0
        
        bit = self.kthGrammar(n-1, (k+1)//2)
        
        if k % 2 == 0:
            # flip bit
            return 1 - bit
        else:
            return bit
        
        
        
            