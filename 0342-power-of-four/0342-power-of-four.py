class Solution:
    def isPowerOfFour(self, n: int) -> bool:
        
        # base case: when n reaches 4 or 1
        if n == 1:
            return True
        
        if(n < 4):
            return False
        
        # Recusive case: call function with the next n/4 
        return self.isPowerOfFour(n/4)