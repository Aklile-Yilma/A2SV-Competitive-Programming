class Solution:
    def hasAlternatingBits(self, n: int) -> bool:
        
        prev = 1 if n % 2 != 0 else 0
        while n != 0:
            n = n >> 1
            curr =  1 if n % 2 != 0 else 0
            if prev == curr:
                return False
            prev = curr
            
        return True
            
            
      